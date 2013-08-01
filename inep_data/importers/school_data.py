from ..models import *

class SchoolDataImporter(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self):
        with open(self.file_path) as file:
            for line in file:
                state_acronymn, schools_city_code, city_name, school_id, school_name = line.split(",")
                state_id = schools_city_code[0:2]
                city_id = schools_city_code[2:6]

                school = School.objects(code = school_id).first()

                if not school: continue

                state = State.objects(code = state_id).first()

                if not state:
                    state = State(code = state_id)
                    state.acronym = state_acronymn

                state.scores = [x + y for x, y in zip(state.scores, school.scores)]
                state.save()

                city = City.objects(code = city_id).first()

                if not city:
                    city = City(code = city_id)
                    city.state_code = state_id
                    city.name = city_name
                    city.state = state

                city.scores = [x + y for x, y in zip(city.scores, school.scores)]
                city.save()

                school.name = school_name
                school.city = city
                school.state = state
                school.save()
