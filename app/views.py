from flask import Flask, render_template, session, redirect, url_for, flash
from app import app, forms, models

@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        user = models.User.query.filter_by(username = login_form.username.data).first()
        if user:
            # Used to display user-specific nav items
            session['logged_in'] = True
            return redirect(url_for('create'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=login_form)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    form = forms.CreateForm()
    if form.validate_on_submit():
        # TODO: If save was a success, inform user
        # Otherwise report error message.
        flash('The form has been submitted successfully.')
    return render_template('create.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
