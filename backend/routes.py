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
from classes.RobotAdapter import Robot

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
        return Response(status= 200)
    else:
        return Response(status= 404)

if __name__ == "__main__":
    app.run()

