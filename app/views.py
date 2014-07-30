from flask import render_template, redirect, url_for, flash, Blueprint
from app import forms, models, db, login_manager
from flask.ext.login import login_user, login_required, logout_user
import datetime

bp = Blueprint('app', __name__)


@login_manager.user_loader
def load_user(username):
    return models.User.query.get(username)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(url_for('app.create'))
    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = forms.CreateForm()
    if form.validate_on_submit():
        dob = datetime.datetime.strptime(form.dob.data, "%d/%m/%Y")
        # Prefer international format as that's what is used by SMS APIs.
        mobile = form.mobile.data.replace('07', '447')
        # Create a patient from user input
        patient = models.Patient(forename=form.forename.data,
                                 surname=form.surname.data,
                                 dob=dob, mobile=mobile)
        # Add patient data to database
        db.session.add(patient)
        db.session.commit()
        # Reset the form & redirect to self.
        flash('The form has been submitted successfully.')
        form.reset()
    return render_template('create.html', form=form)


@bp.app_errorhandler(404)
def page_not_found(e):
    flash('Whoops, something went wrong.'
          'You have been taken back to the login screen.')
    return render_template('404.html'), 404
