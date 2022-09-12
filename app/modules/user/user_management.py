import string
import random
from app.model.db import ConnectDB


class UserManagement:

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def return_user_from_class(self):
        return {"status": "success", "username": self.username}

    def return_user_from_function(self, data):
        return {"status": "success", "data": data}