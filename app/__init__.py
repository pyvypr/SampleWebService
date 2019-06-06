from flask import Flask

app = Flask(__name__)

from VyPR.init_verification import Verification
verification = Verification(app)

from app import routes
