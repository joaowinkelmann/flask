import json
from flask import Flask, request, jsonify

from dbController import dbController as controller
from databaseBuilder import databaseBuilder as builder

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ws', methods=["POST", "GET"])
def ws():
    if request.method == "POST":
        print(request.get_data())
        data = request.get_json()
        #sanitize data, check if all fields are present
        if (data == None or data['temperature'] == None or data['humidity'] == None or data['dewpoint'] == None or data['pressure'] == None or data['speed'] == None or data['direction'] == None or data['datetime'] == None):
            return "False"
        controller.insert(data['temperature'], data['humidity'], data['dewpoint'], data['pressure'], data['speed'], data['direction'], data['datetime'])
        return json.dumps(data)
    else:
        return json.dumps(controller.get())
    
@app.route('/build', methods=["PUT"])
def build():
    builder.build()
    return "Base de dados construída com sucesso"

if __name__ == '__main__':
    app.run()