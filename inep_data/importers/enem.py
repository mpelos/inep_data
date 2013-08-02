import os
from multiprocessing import Process, Queue
from mongoengine import NotUniqueError

from ..enem_parser import EnemParser
from ..models import *

class EnemSchoolImporter(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self, number_of_workers = 2):
        with open(self.file_path) as file:
            queue = Queue(number_of_workers)
            workers = []

            # Create the workers
            for i in range(number_of_workers):
                worker = Process(target = self.process_data, args = (queue, ))
                workers.append(worker)
                worker.start()

            for line in file: queue.put(line)

            # Wait the workers consume the queue and terminate them
            while True:
                if queue.empty():
                    for worker in workers: worker.terminate()
                    break

    def process_data(self, queue):
        parser = EnemParser()

        while True:
            data = parser.parse(queue.get())

            if data["scores"]["mathematics"] and data["school_id"]:
                scores_range = data["scores"]["mathematics"] // 50
                if scores_range == 20: scores_range -= 1

                # MongoDB prevents the workers to save the same school twice.
                # When the workers tries to save the same data simultaneously
                # just one will save and the other will try again.
                while True:
                    try:
                        school = School.objects(code = data["school_id"]).first() or \
                            School(code = data["school_id"])
                        school.city_code = data["city_id"]
                        school.state_code = data["state_id"]
                        school.scores[scores_range] += 1
                        school.save()
                    except NotUniqueError:
                        continue
                    else:
                        break
