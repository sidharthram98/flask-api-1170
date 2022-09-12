from pymongo import MongoClient


class ConnectDB:
    def __init__(self):
        self.connection = None
        self.collection = None

    def connect_db(self, db='', collection=''):
        connection = MongoClient(host="127.0.0.1", port=27017)
        self.connection = connection.test_db
        return self.connection
