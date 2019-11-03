from root import db
from datetime import datetime
from root import admin,ModelView,UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    app = db.Column(db.String(20))
    env = db.Column(db.String(20))
    machine = db.Column(db.String(20))
    ip = db.Column(db.String(20))
    hostuser = db.Column(db.String(20))
    hostpass = db.Column(db.String(20))
    weburl = db.Column(db.String(70))
    webproxyurl = db.Column(db.String(70))
    webuser = db.Column(db.String(20))
    webpass = db.Column(db.String(20))
    dbhost = db.Column(db.String(20))
    dbip = db.Column(db.String(20))
    dbuser = db.Column(db.String(20))
    dbpass = db.Column(db.String(20))
    dbport = db.Column(db.String(20))
    dbsid = db.Column(db.String(20))
    certstorepath = db.Column(db.String(80))
    certtype = db.Column(db.String(20))
    certstorepass = db.Column(db.String(20))
    certkeypass = db.Column(db.String(20))
    dateupdated = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    updatedby = db.Column(db.String(20))
    other_details = db.Column(db.String(500))

    def __repr__(self):
        return f"User('{self.id}', '{self.app}', '{self.env}','{self.machine}', '{self.ip}', '{self.hostuser}', '{self.hostpass}','{self.weburl}','{self.webproxyurl}', '{self.webuser}','{self.webpass}','{self.dbhost}','{self.dbip}','{self.dbuser}','{self.dbpass}','{self.dbport}','{self.dbsid}','{self.certstorepath}','{self.certtype}','{self.certstorepass}','{self.certkeypass}','{self.dateupdated}','{self.updatedby}','{self.other_details}')"

class MyModelView(ModelView):
    def is_accessible(self):
        return False

admin.add_view(ModelView(User,db.session))
