from app import models
from flask.ext.wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import TextField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Required
import datetime


class LoginForm(Form):
    username = TextField('Username: ', [DataRequired(
        message='You must provide a username.'),
        Length(min=3, max=25)])
    password = PasswordField('Password', [DataRequired(
        message='You must provide a password.'),
        Length(min=4, max=40)])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        # Use the validators defined above first, e.g. empty fields.
        if not Form.validate(self):
            return False

        self.user = models.User.query.filter_by(
            username=self.username.data).first()

        if not self.user:
            self.username.errors.append('Unknown username provided.')

        if self.user and not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password provided.')

        if self.username.errors or self.password.errors:
            return False
        return True


class CreateForm(Form):
    forename = StringField('Forename: ', [Required(
        message='A forename must be provided')])
    surname = StringField('Surname: ', [Required(
        message='A surname must be provided.')])
    dob = StringField('D.O.B:', [Required(
        message='A date of birth must be provided in format DD/MM/YYYY.')])
    mobile = StringField('Mobile number: ', [Required(
        message='A mobile number beginning with 07 must be provided.')])

    def validate(self):
        if not Form.validate(self):
            return False

        if not self.forename.data.isalpha():
            self.__reset_field(self.forename,
                               "First name must contain only letters.")

        if not self.surname.data.isalpha():
            self.__reset_field(self.surname,
                               "Last name must contain only letters.")

        try:
            datetime.datetime.strptime(self.dob.data, "%d/%m/%Y")
        except ValueError:
            self.__reset_field(self.dob, "D.O.B format must be DD/MM/YYYY.")

        mobile = self.mobile.data
        if len(mobile) < 7 or len(mobile) > 11:
            self.__reset_field(self.mobile,
                               "Mobile number must between length 7 and 11")

        if mobile[0:2] != '07':
            self.__reset_field(self.mobile, "Mobile number must begin with 07")

        # Validate the UNIQUE mobile number against the DB.
        if models.Patient.query.get(self.mobile.data):
            self.__reset_field(self.mobile,
                               "A patient with that number already exists.")

        if self.forename.errors or self.surname.errors \
                or self.dob.errors or self.mobile.errors:
            return False
        return True

    def __reset_field(self, field, message):
        field.data = ''
        field.errors.append(message)

    def reset(self):
        self.process(MultiDict([]))
