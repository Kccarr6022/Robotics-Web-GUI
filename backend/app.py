###############################################
# App
# --------------------
#
# This file is referenced by routes.py
#
###############################################

# Import the required packages
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
# import config
import os

load_dotenv()

# init cross-origin
cors = CORS()

def create_app():
    # Initialize application
    """Application-factory pattern"""
    app = Flask(__name__)

    cors.init_app(app)

    return app
