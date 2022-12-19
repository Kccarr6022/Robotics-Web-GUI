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
from app import create_app,db

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

@app.route('/', methods=['GET'])
def base():
    return Response(message="working route", status= 200)