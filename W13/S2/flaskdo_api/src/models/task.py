from mongoengine import *
from datetime import datetime


class Task(Document):
    title = StringField(max_length=200, required=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.utcnow())
    tasklist_id = StringField()
