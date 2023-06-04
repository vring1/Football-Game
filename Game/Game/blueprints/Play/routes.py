from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user

from Game.forms import UserLoginForm, UserSignupForm
from Game.queries import get_user_by_name, insert_user
from Game.models import User

Play = Blueprint('Login', __name__)


@Play.route("/")
@Play.route("/home")
def home():
    return render_template('pages/home.html')