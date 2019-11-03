from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask_login import UserMixin




app = Flask(__name__)
app.config['SECRET_KEY'] = '15e168ef54456968fd3cf1ee8aa4aee8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///envdetails.db'
db = SQLAlchemy(app)
admin = Admin(app)


from root import routes
