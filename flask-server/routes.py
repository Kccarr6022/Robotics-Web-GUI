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
from flask import Blueprint, render_template, url_for
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

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/gui')
def login():
    return render_template('roboticscontrol.html')

@app.route('/video_feed')
def video_feed():
    pass

if __name__ == "__main__":
    app.run(debug=True)

