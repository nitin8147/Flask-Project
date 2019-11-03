from flask import render_template,url_for, flash, redirect,request,session
from functools import wraps
from root import app, db
from root.models import User
from root.forms import RegistrationForm, LoginForm, UpdateForm

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    global auth
    auth="False"
    form = LoginForm()
    if form.validate_on_submit():
        user = request.form['username']
        password = request.form['password']
        if user == 'Admin' and password == 'Admin':
            session['user'] = request.form['username']
            auth="true"
            flash(f'Login Successfull !!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Invalid Credentials !! Please try again','danger')
    return render_template('login.html',form=form,auth=auth)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
@is_logged_in
def logout():
    session.pop('user', None)
    flash('You have successfully logged out !!', 'success')
    return redirect(url_for('login'))

@app.route("/home",methods=['GET','POST'])
@is_logged_in
def home():
    global form,app,env,showdt,auth
    form = UpdateForm()
    if request.method == 'POST' and request.form['action'] == 'Search':
        app = request.form.get('appselect')
        env = request.form.get('envselect')
        showdt = User.query.filter_by(app=app,env=env).first()
        return redirect(url_for('appdetails'))
    if request.method == 'POST' and request.form['action'] == 'Update':
        app = request.form.get('appselect')
        env = request.form.get('envselect')
        showdt = User.query.filter_by(app=app,env=env).first()
        form.Other_Details.data = showdt.other_details
        return redirect(url_for('update'))
    return render_template('selapp.html',form=form,auth=auth)



@app.route("/appdetails",methods=['GET','POST'])
@is_logged_in
def appdetails():
    global app,env,form,showdt,auth
    return render_template('appdetails.html',showdt=showdt,form=form,auth=auth)

@app.route("/update",methods=['GET','POST'])
@is_logged_in
def update():
    global app,env,showdt,form,auth
    if request.method == 'POST' and request.form['action'] == 'Submit':
        row_to_update = User.query.filter_by(app=app,env=env).first()
        detail_to_update = {'machine': request.form['Machine_Name'],'ip': request.form['IPP_ADD'],'hostuser': request.form['Machine_User'],'hostpass': request.form['Machine_Password'],
        'webuser': request.form['Weblogic_User'],'webpass': request.form['Weblogic_Password'],'weburl': request.form['Weblogic_URL'],'webproxyurl': request.form['Weblogic_Proxy_URL'],
        'dbhost': request.form['Database_Host'],'dbip': request.form['Database_IP'],'dbuser': request.form['Database_User'],'dbpass': request.form['Database_Password'],
        'dbport': request.form['Database_Port'],'dbsid': request.form['Database_SID'],'certstorepath': request.form['Cert_Store_Path'],
        'certtype': request.form['Cert_Type'],'certstorepass': request.form['Cert_Store_Pass'],'certkeypass': request.form['Cert_Key_Pass'],'other_details': request.form['Other_Details']}

        for key,value in detail_to_update.items():
            setattr(row_to_update, key, value)
            db.session.commit()
        print("Submit Successfull")

        flash('Update Successfull !!', 'success')
        return redirect(url_for('home'))

    form.Other_Details.data = showdt.other_details
    return render_template('update.html',title='Update Details', form=form,showdt=showdt,auth=auth)
