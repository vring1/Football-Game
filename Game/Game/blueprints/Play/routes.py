from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
import random
from Game.forms import UserLoginForm, UserSignupForm, PlayForm
from Game.queries import get_latest_round ,get_all_clubs_by_country_id,insert_game_round, get_user_by_name, insert_user, update_user, get_all_countries, insert_game, complete_game, get_next_seqeuence_id, get_game_by_status
from Game.models import User

Play = Blueprint('Play', __name__)


@Play.route("/play", methods=['GET', 'POST'])
#@loginrequired
def play():
    form = PlayForm()
    title = 'Player1 should choose a player'
    player1 = "John"
    player2 = "Ali"
    play_game(player1,player2)


    return render_template('pages/game.html', form=form, title=title)
    

def init_game():

    #INSERT userid in game table (1 & 2)
    user1_id = 1
    user2_id = 2
    #update_user(#user1, 1)
    #update_user(#user2, 2)
        
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

    insert_game_round(1, game.id, user1_club.id, user2_club.id)


def play_game():    
    # Get started game with status "STARTED"
    game = get_game_by_status('STARTED')

    round = get_round(game)
    #Game_round table:
    active_player = None
    if round.user1_player_guess == None:
        active_player = game.user1_id

    #Insert gameid from game table


    #LOOP (in round table):
        #if end_of_round:
            # Get value from user1_correct_guess & user2_correct_guess

        #    if user1_correct_guess and not user2_correct_guess:
        #        user1 won
        #    if user2_correct_guess and not user1_correct_guess:
        #        user2 won

        #insert round number

        #Insert user1_club_id and user2_club_id

        #Insert user1_player_guess

        #Evaluate the guess and insert true/false in user1_correct_guess

        #Insert user2_player_guess

        #Evaluate the guess and insert true/false in user2_correct_guess

    # END GAME with query

    #complete_game() #sæt status for game to COMPLETED

def get_round(game):
    game_round = get_latest_round(game.id)
    if game_round.status == 'COMPLETED': 
        #TODO: SØRG FOR AT SAMME KLUB IKKE KAN VÆLGES TO GANGE
        user1_possible_clubs = get_all_clubs_by_country_id(game.user1_country.id)
        user2_possible_clubs = get_all_clubs_by_country_id(game.user2_country.id)
        user1_club = random.choice(user1_possible_clubs)
        user2_club = random.choice(user2_possible_clubs)
        insert_game_round(game_round.round+1, game.id, user1_club.id, user2_club.id)
    return get_latest_round(game.id)