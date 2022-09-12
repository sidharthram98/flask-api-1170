from datetime import datetime, timedelta

from flask import request

from app.model.db import ConnectDB


class MeetingService:

    def __init__(self):
        self.collectionName = "meetings"

    def save_meetings(self, meetings_list):
        """
        A method to save multiple meeting objects to the database collection meetings
        :param meetings_list:
        :return: response
        """
        connection = ConnectDB()
        mongodb_connection = connection.connect_db()
        meetings = mongodb_connection[self.collectionName]
        response = {}
        for meeting in meetings_list:
            query = {"topic": meeting["topic"]}
            docs = meetings.find(query)
            if docs.count() > 0:
                response[meeting["topic"]] = "DUPLICATE"
            else:
                meeting["date_ts"] = datetime.strptime(meeting["date_ts"], "%Y-%m-%d %H:%M:%S")
                meetings.insert_one(meeting)
                response[meeting["topic"]] = "SUCCESS"
        return response


    save_meetings.__doc__ = "A method to save multiple meeting objects to the database collection meetings"

    def search_date(self, date):
        # User input is from date
        from_date = datetime.strptime(date, "%Y-%m-%d")
        # To date is from date + 1
        to_date = from_date + timedelta(days=1)
        connection = ConnectDB()
        mongodb_connection = connection.connect_db()
        meetings = mongodb_connection[self.collectionName]
        # Find meetings between the from date and to date
        query = {"date_ts": {"$gte": from_date, "$lte": to_date}}
        docs = meetings.find(query)
        response = []
        for doc in docs:
            del doc["_id"]
            response.append(doc)
        return response

    def search_till_now(self, date):
        connection = ConnectDB()
        mongodb_connection = connection.connect_db()
        meetings = mongodb_connection[self.collectionName]

        # User input is my date
        my_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

        # We need to query 2 times one for less than my_date and more than my_date
        # Get the meetings that are over
        from_date1 = my_date.replace(hour=0, minute=0, second=0, microsecond=0)
        to_date1 = my_date
        query1 = {"date_ts": {"$gte": from_date1, "$lt": to_date1}}
        docs = meetings.find(query1)
        response = {}
        meetings_over = []
        for doc in docs:
            del doc["_id"]
            meetings_over.append(doc)
        response["meetings_over"] = meetings_over

        # Get the meetings that are not over
        from_date2 = my_date
        to_date2 = my_date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        query2 = {"date_ts": {"$gte": from_date2, "$lte": to_date2}}
        docs = meetings.find(query2)
        meetings_left = []
        for doc in docs:
            del doc["_id"]
            meetings_left.append(doc)
        response["meetings_left"] = meetings_left
        return response
