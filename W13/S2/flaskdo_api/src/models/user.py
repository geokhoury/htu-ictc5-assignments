from mongoengine import *
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256


class User(Document):
    username = StringField()
    password = StringField()
    first_name = StringField()
    last_name = StringField()
    tasklists = ListField(StringField())
    created_at = DateTimeField()

    def add_tasklist(self, tasklist_id):
        self.tasklists.append(tasklist_id)

    @staticmethod
    def generate_hash(password):
        # Returns the hash value for the password
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        # Verifies the hash against the password
        return sha256.verify(password, hash)

    @staticmethod
    def authenticate(username, password):
        user = User.objects(username=username).first()

        if user:
            return User.verify_hash(password, user.password)
        else:
            return None
