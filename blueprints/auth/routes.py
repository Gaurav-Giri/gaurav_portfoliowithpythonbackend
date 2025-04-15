from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from forms import LoginForm
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home.index'))
        flash('Invalid username or password', 'error')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home.index'))