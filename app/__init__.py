from flask import Flask

app = Flask(__name__)

from VyPR import Monitor
vypr = Monitor()
vypr.initialise(app)

from app import routes
