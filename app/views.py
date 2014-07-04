from flask import Flask, render_template, session, redirect, url_for, flash
from app import app, forms


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        # TODO: validate user against db
        flash('The form has been submitted successfully.')
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    form = forms.CreateForm()
    if form.validate_on_submit():
        # TODO: If save was a success, inform user
        # Otherwise report error message.
        flash('The form has been submitted successfully.')
    return render_template('create.html', form=form)
