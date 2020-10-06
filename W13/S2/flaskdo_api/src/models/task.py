from mongoengine import *
from datetime import datetime
from .tasklist import TaskList


class Task(Document):
    title = StringField(max_length=200, required=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.utcnow())
    tasklists = ListField(ReferenceField(TaskList))
