import logging, os
from flask import Flask
from flask_mail import Mail
logger = logging.getLogger('python')
logger.setLevel(logging.WARNING)
mail = Mail()
app = Flask(__name__)
app.config.from_object('config.{}Config'.format(os.environ.get('SERVER_ENV', 'Development')))
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].format(
	os.environ.get('DB_USER'),
	os.environ.get('DB_PASS'),
	os.environ.get('DB_HOST'),
	os.environ.get('DB_NAME')
	)
app.config['APP_NAME'] = app.config['APP_NAME'].format(os.environ.get('NAME', 'API'))
app.config['SECRET_KEY'] = app.config['SECRET_KEY'].format(os.environ.get('SECRET_KEY', 'SECRET'))
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECURITY_PASSWORD_SALT'].format(os.environ.get('SECURITY_PASSWORD_SALT'))
