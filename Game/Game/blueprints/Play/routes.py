from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user

from Game.forms import UserLoginForm, UserSignupForm, PlayerForm
from Game.queries import get_user_by_name, insert_user
from Game.models import User

Play = Blueprint('Play', __name__)


@Play.route("/")
@Play.route("/home")
def home():
    return render_template('pages/home.html')

@Play.route("/play", methods=['GET', 'POST'])
def player1plays():
    form = PlayerForm()
    title = 'Player1/2 should choose a player'
    return render_template('pages/game.html', form=form, title=title)
    