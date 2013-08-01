import os
from mongoengine import NotUniqueError

from ..enem_parser import EnemParser
from ..models import *

class EnemSchoolImporter(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self, start_line = 0, line_jump = 1):
        parser = EnemParser()
        line_counter = line_jump - 1

        with open(self.file_path, "r") as file:
            # jump to start line
            for i in range(start_line): file.readline()
            jump_counter = 0

            for line in file:
                if jump_counter < line_jump - 1:
                    jump_counter += 1
                    continue
                else:
                    jump_counter = 0

                data = parser.parse(line)

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

    def parallel_import(self, workers = 2):
        children = []

        for i in range(workers):
            pid = os.fork()

            if pid > 0:
                children.append(pid)
            else:
                self.import_data(i, workers)
                os._exit(0)

        for child in children: os.waitpid(child, 0)
