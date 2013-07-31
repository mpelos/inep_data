import sys

from enem_parser import EnemParser
from models import *

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Erro: Especifique o arquivo de dados do ENEM"
    else:
        with open(sys.argv[1], "r") as file:
            parser = EnemParser()

            for line in file:
                data = parser.parse(line)

                if data["scores"]["mathematics"]:
                    scores_range = data["scores"]["mathematics"] // 100
                    if scores_range == 10: scores_range -= 1

                    if data["state_id"]:
                        state = State.objects(code = data["state_id"]).first() or \
                            State(code = data["state_id"])

                        state.acronym = data["state"]
                        state.scores[scores_range] += 1
                        state.save()

                    if data["city_id"]:
                        city = City.objects(code = data["city_id"]).first() or \
                            City(code = data["city_id"])

                        city.state_code = data["state_id"]
                        city.name = data["city"]
                        city.scores[scores_range] += 1
                        city.save()

                    if data["school_id"]:
                        school = School.objects(code = data["school_id"]).first() or \
                            School(code = data["school_id"])

                        school.city_code = data["city_id"]
                        school.state_code = data["state_id"]
                        school.scores[scores_range] += 1
                        school.save()
