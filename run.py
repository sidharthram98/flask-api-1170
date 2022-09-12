from app import app
from flask import request
import requests

@app.route('/carrecognizer/initialize', methods=['POST','GET'])
def process_data():
   data = {"status": "success"}
   return data, 200
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1170)