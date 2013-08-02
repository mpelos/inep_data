import os
import yaml
from mongoengine import *

connect("inep_data_development", host = os.environ.get('MONGOHQ_URL', 'localhost'))

with open("config.yml") as config:
    scores_ranges = yaml.load(config)["scores_ranges"]

scores = [{ "range": r, "value": 0 } for r in scores_ranges]

class State(Document):
    code = IntField(required=True, unique=True)
    acronym = StringField();
    scores = ListField(default = scores)

class City(Document):
    code = IntField(required=True, unique=True)
    state = ReferenceField(State)
    name = StringField()
    scores = ListField(default = scores)

class School(Document):
    code = IntField(required=True, unique=True)
    city = ReferenceField(City)
    state = ReferenceField(State)
    name = StringField()
    scores = ListField(default = scores)
