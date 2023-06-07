from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
import random
import psycopg2
from Game.forms import PlayForm, StartNewGameForm, StartGameForm

from Game.queries import get_all_rounds, update_game_round, get_played_by_player_name_and_country_id_and_club_id, \
    get_all_clubs, get_latest_round, get_all_clubs_by_country_id, insert_game_round, get_user_by_name, insert_user, \
    update_user, get_all_countries, insert_game, complete_game, get_next_seqeuence_id, get_game_by_status
from Game.models import User

Play = Blueprint('Play', __name__)


@Play.route('/', methods=['GET', 'POST'])
def home():
    form = StartGameForm()
    if form.validate_on_submit():
        return redirect(url_for('Play.play'))
    return render_template('pages/home.html', form=form)


@Play.route("/play", methods=['GET', 'POST'])
def play():
    form = PlayForm()
    game = get_game_by_status('STARTED')
    if not game:
        init_game()
        game = get_game_by_status('STARTED')

    game_round = get_latest_round(game.id)

    if form.validate_on_submit():
        playername = form.playername.data
        winner = None
        # Check hvis tur det er...
        if game_round.user1_player_guess is None:
            # player1's tur
            player_exists = get_played_by_player_name_and_country_id_and_club_id(playername, game.country1_id,
                                                                                 game_round.user1_club_id)
            update_game_round(game_round.round_number, game.id, playername, 'CORRECT' if player_exists else 'WRONG', None,
                              None, 'STARTED')
        else:
            player_exists = get_played_by_player_name_and_country_id_and_club_id(playername, game.country2_id,
                                                                                 game_round.user2_club_id)
            update_game_round(game_round.round_number, game.id, game_round.user1_player_guess, game_round.user1_correct, playername,
                              'CORRECT' if player_exists else 'WRONG', 'COMPLETED')
            game_round = get_latest_round(game.id)
            if game_round.user1_correct == 'CORRECT' and game_round.user2_correct == 'WRONG':
                # player1 wins
                winner = 'Player 1'
            if game_round.user1_correct == 'WRONG' and game_round.user2_correct == 'CORRECT':
                winner = 'Player 2'
            if winner:
                return redirect(url_for('Play.game_completed'))
            else:
                result = make_new_round(game.id, game_round.round_number + 1, game.country1_id, game.country2_id)
                if not result:
                    return redirect(url_for('Play.no_more_clubs'))

        rounds = get_all_rounds(game.id)
        game_round = get_latest_round(game.id)
        return render_template('pages/game.html', form=form, game=game, rounds=rounds, game_round=game_round,
                               winner=winner)

    rounds = get_all_rounds(game.id)
    game_round = get_latest_round(game.id)
    return render_template('pages/game.html', form=form, game=game, rounds=rounds, game_round=game_round)


def init_game():
    # INSERT userid in game table (1 & 2)
    user1_id = 1
    user2_id = 2

    # SELECT ALL countries and load into array
    countries = get_all_countries()
    user1_country = random.choice(countries)
    while True:
        user2_country = random.choice(countries)
        if user2_country != user1_country:
            break
    # insert random country in game-table (user1_country and user2_country)
    insert_game(user1_id, user2_id, user1_country.id, user2_country.id)
    game = get_game_by_status('STARTED')
    result = make_new_round(game.id, 1, user1_country.id, user2_country.id)
    if not result:
        return redirect(url_for('Play.no_more_clubs'))


def make_new_round(game_id, game_round, country1_id, country2_id):
    try:
        user1_possible_clubs = get_all_clubs_by_country_id(game_id, country1_id, 'User1')
        user1_club = random.choice(user1_possible_clubs)
        user2_possible_clubs = get_all_clubs_by_country_id(game_id, country2_id, 'User2')
        user2_club = random.choice(user2_possible_clubs)
        insert_game_round(game_round, game_id, user1_club.club_id, user2_club.club_id)
        return True
    except Exception as err:
        print("Oops!  Unexpected error: ", err)
        return False



@Play.route("/game_completed", methods=['GET', 'POST'])
def game_completed():
    form_game_completed = StartNewGameForm()
    game = get_game_by_status('STARTED')
    rounds = get_all_rounds(game.id)
    last_round = get_latest_round(game.id)
    if last_round.user1_correct == 'CORRECT':
        winner = "User1"
    if last_round.user2_correct == 'CORRECT':
        winner = "User2"
    if form_game_completed.validate_on_submit():
        complete_game(game.id)
        return redirect(url_for('Play.play'))

    return render_template('pages/game_completed.html', form=form_game_completed, title="Game completed", game=game,
                           rounds=rounds, winner=winner)


@Play.route("/no_more_clubs", methods=['GET', 'POST'])
def no_more_clubs():
    form = StartGameForm()
    if form.validate_on_submit():
        game = get_game_by_status('STARTED')
        complete_game(game.id)
        return redirect(url_for('Play.play'))
    return render_template('pages/no_more_clubs.html', form=form)