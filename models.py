from mongoengine import *

connect("inep_data_development")

class School(Document):
    code = IntField(required=True)
    city_code = IntField()
    state_code = IntField()
    name = StringField()
    scores = ListField(default = [0 for n in xrange(0,10)])

class City(Document):
    code = IntField(required=True)
    state_code = IntField()
    name = StringField()
    scores = ListField(default = [0 for n in xrange(0,10)])

class State(Document):
    code = IntField(required=True)
    acronym = StringField();
    scores = ListField(default = [0 for n in xrange(0,10)])
