from app import db


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(64),  nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(192), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return 'The users name is: %r' % self.username


class Patient(db.Model):
    __tablename__ = 'patients'

    forename = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    dob = db.Column(db.Date)
    mobile = db.Column(db.String(30), nullable=False, unique=True, primary_key=True)

    def __init__(self, forename, surname, dob, mobile):
        self.forename = forename
        self.surname = surname
        self.dob = dob
        self.mobile = mobile

    def __repr__(self):
        return 'The patients name & mobile number are: %r %r, %r' % (self.forename, self.surname, self.mobile)
