from flask import Flask

p_app = Flask(__name__)
p_app.config.from_object('config')

from app import views
