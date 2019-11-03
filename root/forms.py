from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username =  StringField('UserName', validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    Application_Name = StringField('Application_Name')
    Machine_Name = StringField('Machine_Name')
    IPP_ADD = StringField('IPP_ADD')
    Machine_User = StringField('Machine_User')
    Machine_Password = StringField('Machine_Password')
    Weblogic_User = StringField('Weblogic_User')
    Weblogic_Password = StringField('Weblogic_Password')
    Weblogic_URL = StringField('Weblogic_URL')
    Weblogic_Proxy_URL = StringField('Weblogic_Proxy_URL')
    Database_Host = StringField('Database_Host')
    Database_IP = StringField('Database_IP')
    Database_User = StringField('Database_User')
    Database_Password = StringField('Database_Passowrd')
    Database_Port = StringField('Database_Port')
    Database_SID = StringField('Database_SID')
    Cert_Store_Path = StringField('Cert_Store_Path')
    Cert_Type = StringField('Cert_Type')
    Cert_Store_Pass  = StringField('Cert_Store_Pass')
    Cert_Key_Pass = StringField('Cert_Key_Pass')
    Other_Details = TextAreaField('Other_Details')
    submit = SubmitField('Submit')
