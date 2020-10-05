from mongoengine import *
from datetime import datetime


class TaskList(Document):
    name = StringField()
    description = StringField()
    owner_id = StringField()
    created_at = DateTimeField()
