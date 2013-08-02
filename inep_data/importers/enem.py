from multiprocessing import Process, Queue
from pymongo import MongoClient
from mongoengine import NotUniqueError
import yaml

from ..enem_parser import EnemParser
from ..models import School

class EnemSchoolImporter(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self, number_of_workers = 2):
        db = MongoClient()["inep_data_development"]

        with open(self.file_path) as file:
            queue = Queue(number_of_workers)
            workers = []

            # Create the workers
            for i in range(number_of_workers):
                worker = Process(target = self.process_data, args = (db, queue))
                workers.append(worker)
                worker.start()

            for line in file: queue.put(line)

            # Wait the workers consume the queue and terminate them
            while True:
                if queue.empty():
                    for worker in workers: worker.terminate()
                    break

    def process_data(self, db, queue):
        parser = EnemParser()
        schools = db.school

        with open("config.yml") as config:
            scores_ranges = yaml.load(config)["scores_ranges"]

        while True:
            data = parser.parse(queue.get())

            if data["scores"]["mathematics"] and data["school_id"]:
                range_index = data["scores"]["mathematics"] // (1000 / len(scores_ranges))
                if range_index == 20: range_index -= 1

                # MongoDB prevents the workers to save the same school twice.
                # When the workers tries to save the same data simultaneously
                # just one will save and the other will try again.
                try:
                    School(code = data["school_id"]).save()
                except NotUniqueError:
                    pass

                schools.update(
                    { "code": data["school_id"], "scores.range": scores_ranges[range_index] },
                    { "$inc": { "scores.$.value": 1 } }
                )
