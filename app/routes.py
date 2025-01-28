from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User
from app.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("name", __name__)


@bp.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('dashboard.html') 
    return render_template('base.html')  


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('name.dashboard')) 
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Konto zostało pomyślnie utworzone. Możesz się zalogować.")
        return redirect(url_for('name.login'))
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('name.dashboard'))  
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Zalogowano pomyślnie")
            return redirect(url_for('name.dashboard')) 
        else:
            flash("Niepoprawne dane logowania.")
    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Wylogowano pomyślnie")
    return redirect(url_for('name.login'))


@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)
