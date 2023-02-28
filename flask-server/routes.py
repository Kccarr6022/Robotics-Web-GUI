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
from flask import Blueprint, render_template, url_for, Response
from app import create_app
from classes.spot import Spot
import bosdyn.client

####################################
#
# Global variables
#
####################################
# Create an application instance
app = create_app()
spot = Spot(host='ip address here', username='username here', password='password')

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

@app.route("/video_feed")
def video_feed():
    """return the response generated along with the specific media type (mime type)"""
    return Response(spot.video_streamer.generate(), mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

