from app import db


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(64),  nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(192), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.email = password

    def __repr__(self):
        return 'The users name is: %r' % self.name


class Patient(db.Model):
    __tablename__ = 'patients'

    # Used to determine which nurse triaged a patient.
    # clientname = db.Column(db.String(64), db.ForeignKey('users.username'))
    mobile = db.Column(db.Integer, unique=True, primary_key=True)
    forename = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    dob = db.Column(db.Date)

    def __init__(self, mobile, forename, surname, dob):
        self.mobile = mobile
        self.forename = forename
        self.surname = surname
        self.dob = dob

    def __repr__(self):
        return 'The mobile number and name are: %r, %r %r' % (self.mobile, self.forename, self.surname)
