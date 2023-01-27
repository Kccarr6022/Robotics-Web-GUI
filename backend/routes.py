###############################################
# Routes
# --------------------
#
# This is where the backend starts and builds our application.
# This is one of the most important files for the backend.
# It houses all the api routes as well as their functionality.
#
###############################################

####################################
#
# Imports
#
####################################
from flask import current_app,jsonify, make_response, flash, request, redirect, url_for, session, Response, copy_current_request_context
from app import create_app
from classes.robot_adapter import Robot
import bosdyn.client

####################################
#
# Global variables
#
####################################
# Create an application instance
app = create_app()

####################################
#
# Functions
#
####################################


####################################
#
# Routes
#
####################################

@app.route('/api/login', methods=['POST'])
def base():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        return jsonify({"msg": "Successful login"}), 200 # success
    else:
        return jsonify({"msg": "Wrong username or password"}), 200 # Wrong username or password
        

@app.route('/api/spot/power', methods=['GET'])
def get_spot_power():
    spot_power = True # Function to check power


    return {
        "power": spot_power
    }, 200


@app.route('/api/spot/ping', methods=['GET'])
def get_spot_ping():
    spot_power = True # Function to check power


    return {
        "status": 'Connected'
    }


@app.route('/api/spot/login', methods=['POST'])
def post_spot_login():
    data = request.get_json()

    if data['username']=="admin" and data['password']=="admin": # condition to login
        return {'msg': 'success'}, 200
    else:
        return {'msg': 'not successful'}, 201


if __name__ == "__main__":
    app.run()

