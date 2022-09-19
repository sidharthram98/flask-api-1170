import json
from app import app, cross_origin
from flask import render_template, request, jsonify
from app.modules.user.user_management import UserManagement
from app.model.db import ConnectDB
from datetime import datetime, timedelta
from app.modules.meetingservice.meetingservice import MeetingService


# Services

@app.route("/", methods=["GET"])
def index():
    print request.__dict__
    return render_template("pages/index.html")


@app.route("/api/testGET", methods=["GET"])
def test1():
    return jsonify({"status": "success"})


@app.route("/api/testPOST1", methods=["POST"])
def test2():
    data = json.loads(request.data)
    return jsonify(UserManagement(username=data["username"], password=data["username"]).return_user_from_class())


@app.route("/api/testPOST2", methods=["POST"])
def test3():
    data = json.loads(request.data)
    return jsonify(UserManagement().return_user_from_function(data=data))


@app.route("/meeting/add", methods=["POST"])
def add_meeting():
    meetings = json.loads(request.data)
    meeting_service = MeetingService()
    response = meeting_service.save_meetings(meetings)
    return jsonify(response)


@app.route("/date/search", methods=["GET"])
def search_date():
    d = request.args.get("searchdate")
    meeting_service = MeetingService()
    response = meeting_service.search_date(d)
    return jsonify(response)


@app.route("/date/tillnow", methods=["GET"])
def search_date_time():
    d = request.args.get("searchdate")
    meeting_service = MeetingService()
    response = meeting_service.search_till_now(d)
    return jsonify(response)
