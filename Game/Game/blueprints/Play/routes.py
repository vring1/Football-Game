from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
import random
import psycopg2
#from Game.forms import UserLoginForm, UserSignupForm, PlayForm
from Game.forms import PlayForm, StartNewGameForm

from Game.queries import get_all_rounds, update_game_round, get_played_by_player_name_and_country_id_and_club_id, get_all_clubs ,get_latest_round ,get_all_clubs_by_country_id,insert_game_round, get_user_by_name, insert_user, update_user, get_all_countries, insert_game, complete_game, get_next_seqeuence_id, get_game_by_status
from Game.models import User

Play = Blueprint('Play', __name__)


@Play.route("/play", methods=['GET', 'POST'])
#@loginrequired
def play():
    form = PlayForm()
    title = 'User should choose a player'
    
    game = get_game_by_status('STARTED')
    if not game:
        init_game()
        game = get_game_by_status('STARTED')

    print(game)

    #round = get_round(game)
    round = get_latest_round(game.id)
    if round == None or round.game_round_status == 'COMPLETED': 
        #TODO: SØRG FOR AT SAMME KLUB IKKE KAN VÆLGES TO GANGE
        user1_possible_clubs = get_all_clubs_by_country_id(game.country1_id)
        user2_possible_clubs = get_all_clubs_by_country_id(game.country2_id)
        user1_club = random.choice(user1_possible_clubs)
        user2_club = random.choice(user2_possible_clubs)
        insert_game_round(round.round_number+1, game.id, user1_club.club_id, user2_club.club_id)
        round = get_latest_round(game.id)

    if form.validate_on_submit():
        playername = form.playername.data
        winner = None
        #Check hvis tur det er...
        if round.user1_player_guess == None: 
            #player1's tur
            player_exists = get_played_by_player_name_and_country_id_and_club_id(playername,game.country1_id,round.user1_club_id)
            print(player_exists)
            update_game_round(round.round_number, game.id, playername, 'CORRECT' if player_exists else 'WRONG', None, None, 'STARTED')
            print("user1 round:",round)
            print("game id:",game.id)
        else:
            player_exists = get_played_by_player_name_and_country_id_and_club_id(playername,game.country2_id,round.user2_club_id)
            update_game_round(round.round_number, game.id, round.user1_player_guess, round.user1_correct, playername, 'CORRECT' if player_exists else 'WRONG', 'COMPLETED')
            print("user2 round:",round)
            round = get_latest_round(game.id)
            if round.user1_correct == 'CORRECT' and round.user2_correct == 'WRONG':
                #player1 wins
                winner = 'Player 1'
            if round.user1_correct == 'WRONG' and round.user2_correct == 'CORRECT':
                winner = 'Player 2'
            if winner:
                complete_game(game.id)
            user1_possible_clubs = get_all_clubs_by_country_id(game.country1_id)
            user2_possible_clubs = get_all_clubs_by_country_id(game.country2_id)
            user1_club = random.choice(user1_possible_clubs)
            user2_club = random.choice(user2_possible_clubs)
            insert_game_round(round.round_number+1, game.id, user1_club.club_id, user2_club.club_id)

        rounds = get_all_rounds(game.id)
        round = get_latest_round(game.id)
        return render_template('pages/game.html',form=form, title=title, game=game, rounds=rounds, round=round, winner=winner)

    rounds = get_all_rounds(game.id)
    round = get_latest_round(game.id)
    print(rounds)
    return render_template('pages/game.html',form=form, title=title, game=game, rounds=rounds, round=round)


def init_game():

    #INSERT userid in game table (1 & 2)
    user1_id = 1
    user2_id = 2
        
    #SELECT ALL countries and load into array
    countries = get_all_countries()
    user1_country = random.choice(countries)
    while True:
        user2_country = random.choice(countries)
        if user2_country != user1_country:
            break
    #insert random country in game-table (user1_country and user2_country)
    
    insert_game(user1_id, user2_id, user1_country.id, user2_country.id)

    game = get_game_by_status('STARTED')
    
    user1_possible_clubs = get_all_clubs_by_country_id(user1_country.id)
    user2_possible_clubs = get_all_clubs_by_country_id(user2_country.id)

    user1_club = random.choice(user1_possible_clubs)
    user2_club = random.choice(user2_possible_clubs)

    insert_game_round(1, game.id, user1_club.club_id, user2_club.club_id)
