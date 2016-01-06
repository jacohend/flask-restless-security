import logging
from flask import Flask
from flask_mail import Mail
logger = logging.getLogger('python')
logger.setLevel(logging.WARNING)
mail = Mail()
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
