from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user

from Game.forms import UserLoginForm, UserSignupForm
from Game.queries import get_user_by_name, insert_user
from Game.models import User

Login = Blueprint('Login', __name__)


@Login.route("/")
@Login.route("/home")
def home():
    return render_template('pages/home.html')

#
# @Login.route("/about")
# def about():
#     return render_template('pages/about.html')
#
#
# @Login.route("/style-guide")
# def style_guide():
#     return render_template('pages/style-guide.html')


@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = UserLoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = get_user_by_name(form.name.data)
            if user and user['password'] == form.password.data:
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('Login.home'))
    return render_template('pages/login.html', form=form)


@Login.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = UserSignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_data = dict(name=form.name.data,
                             password=form.password.data)
            user = User(user_data)
            insert_user(user)
            user = get_user_by_name(form.name.data)
            if user:
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('Login.home'))
    return render_template('pages/signup.html', form=form)


@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.login'))
