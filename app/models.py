from app import db, bcrypt
from flask.ext.login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(64), nullable=False,
                         unique=True, primary_key=True)
    password = db.Column(db.String(192), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def get_id(self):
        return unicode(self.username)

    def __repr__(self):
        return 'The users name is: %r' % self.username


class Patient(db.Model):
    __tablename__ = 'patients'

    forename = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    dob = db.Column(db.Integer)
    mobile = db.Column(db.String(30), nullable=False,
                       unique=True, primary_key=True)

    def __repr__(self):
        return 'The patients name & mobile number are: %r %r, %r' \
            % (self.forename, self.surname, self.mobile)
