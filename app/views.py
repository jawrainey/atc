from flask import Flask, render_template, session, redirect, url_for, flash
from app import app, forms, models, db, bcrypt, login_manager
from flask.ext.login import login_user, login_required, logout_user
import datetime


@login_manager.user_loader
def load_user(username):
    return models.User.query.get(username)

@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        user = models.User.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('create'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')


@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    create_form = forms.CreateForm()
    if create_form.validate_on_submit():
        # Create a patient from user input
        patient = models.Patient(forename = create_form.forename.data,
                                 surname = create_form.surname.data,
                                 dob = datetime.datetime.strptime(create_form.dob.data, "%d/%m/%Y"),
                                 mobile = create_form.mobile.data
                                )
        # Add patient data to database
        db.session.add(patient)
        db.session.commit()
        # Reset the form & redirect to self.
        flash('The form has been submitted successfully.')
        create_form.reset()
    return render_template('create.html', form=create_form,error='error')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
