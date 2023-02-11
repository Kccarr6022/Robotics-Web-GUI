
# Import the required packages
from flask import Flask
from dotenv import load_dotenv
import bosdyn.client

load_dotenv()

app = Flask(__name__)

@app.route("/")

app.run(host="0.0.0.0", port="5000")
