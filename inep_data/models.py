import os
from mongoengine import *

connect("inep_data_development", host = os.environ.get('MONGOHQ_URL', 'localhost'))

class State(Document):
    code = IntField(required=True, unique=True)
    acronym = StringField();
    scores = ListField(default = [0 for n in xrange(0,20)])

class City(Document):
    code = IntField(required=True, unique=True)
    state_code = IntField()
    state = ReferenceField(State)
    name = StringField()
    scores = ListField(default = [0 for n in xrange(0,20)])

class School(Document):
    code = IntField(required=True, unique=True)
    city_code = IntField()
    city = ReferenceField(City)
    state_code = IntField()
    state = ReferenceField(State)
    name = StringField()
    scores = ListField(default = [0 for n in xrange(0,20)])
