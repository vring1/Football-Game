from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
import random
from Game.forms import UserLoginForm, UserSignupForm, PlayForm
from Game.queries import get_all_clubs_by_country_id,insert_game_round, get_user_by_name, insert_user, update_user, get_all_countries, insert_game, complete_game, get_next_seqeuence_id, get_game_by_status
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

def play_game():    
    # Get started game with status "STARTED"
    game = get_game_by_status('STARTED')

    round = get_round(game)
    #Game_round table:
    if round.

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

    complete_game() #sæt status for game to COMPLETED


    #conn = psycopg2.connect("dbname=game user=postgres password=postgres host=localhost")

    # Dictionary for player, country and clubs
    #with conn.cursor() as cur:
        # extract a player list from db
    #    cur.execute("SELECT UPPER(full_name), country, STRING_AGG(club, ',') FROM game.viewplayersinclubs GROUP BY UPPER(full_name), country")
    #    result_set = cur.fetchall()
    #    players = {row[0]: [row[1], row[2].split(',')] for row in result_set}
    #    print("Dict: ", players)
    #conn.close()

    # set active player
    active_player = player1

    # først får player1 og player2 tildelt sig et land hver, som de skal gætte spillere fra
    # player1_country = "DENMARK" #get a random country
    # player2_country = "GERMANY"
    player1_country = random.choice([data[0] for data in players.values()])
    print("PLAYER 1 COUNTRY: ", player1_country)

    while True:
        player2_country = random.choice([data[0] for data in players.values()])
        if player2_country != player1_country:
            break
    print("PLAYER 2 COUNTRY: ", player2_country)

    # all clubs associated to the right country given the player
    clubs_player1 = []
    for player, data in players.items():
        if data[0] == player1_country:
            clubs_player1.extend(data[1])
    print("(PLAYER 1) Clubs for", player1_country, ":", clubs_player1)
    # all clubs associated to the right country given the player
    clubs_player2 = []
    for player, data in players.items():
        if data[0] == player2_country:
            clubs_player2.extend(data[1])
    print("(PLAYER 2) Clubs for", player2_country, ":", clubs_player2)

    # keep track of used clubs for each player, such that the players dont get the same clubs again and again
    player1_used_clubs = []
    player2_used_clubs = []

    # GAME LOOP
    end_of_round = False

    while True:
        if end_of_round:
            if player1_guessed_right and not player2_guessed_right:
                print(player1, "WON!!!")
                return
            if player2_guessed_right and not player1_guessed_right:
                print(player2, "WON!!!")
                return

        if active_player == player1:
            end_of_round = False
            # nu får player1 sin klub at vide:
            player1_club = random.choice(
                clubs_player1)  # brug playerhasplayedinclub til at vise Ajax, men ikke spilleren.

            # sørg for at en tidligere brugt klub ikke kan bruges igen
            while True:
                if player1_club in player1_used_clubs:
                    if len(player1_used_clubs) == len(clubs_player1):
                        print("NO MORE CLUBS AVAILABLE FOR PLAYER 1")
                        return
                    player1_club = random.choice(
                        clubs_player1)  # brug playerhasplayedinclub til at vise Ajax, men ikke spilleren.
                else:
                    break
            player1_used_clubs.append(player1_club)
            print("PLAYER 1 USED CLUBS: ", player1_used_clubs)

            print(player1, ", choose a player from", player1_country, ", which has played in", player1_club)
            player1_guess = input().upper()

            player1_guessed_right = False

            # REFACTOR
            for player, data in players.items():
                if player1_guess == player:  # tjek om spilleren findes
                    country = data[0]
                    if player1_country == country:  # tjek om spillere har en relation til det rigtige land
                        clubs = data[1]
                        for club in clubs:
                            if club == player1_club:  # tjek om spilleren også har en relation til det rigtige hold
                                player1_guessed_right = True
                                print("CORRECT")
            active_player = switch_turn(player1)

        if active_player == player2:
            # sørg for at en tidligere brugt klub ikke kan bruges igen
            player2_club = random.choice(clubs_player2)
            while True:
                if player2_club in player2_used_clubs:
                    if len(player2_used_clubs) == len(clubs_player2):
                        print("NO MORE CLUBS AVAILABLE FOR PLAYER 2")
                        return
                    player2_club = random.choice(
                        clubs_player2)  # brug playerhasplayedinclub til at vise Ajax, men ikke spilleren.
                else:
                    break
            player2_used_clubs.append(player2_club)
            print("PLAYER 2 USED CLUBS: ", player2_used_clubs)

            print(player2, ", choose a player from", player2_country, ", which has played in", player2_club)
            player2_guess = input().upper()

            player2_guessed_right = False
            # check om player2 har gættet på en fra det rigtige land
            for player, data in players.items():
                if player2_guess == player:  # tjek om spilleren findes
                    country = data[0]
                    if player2_country == country:  # tjek om spillere har en relation til det rigtige land
                        clubs = data[1]
                        for club in clubs:
                            if club == player2_club:  # tjek om spilleren også har en relation til det rigtige hold
                                player2_guessed_right = True
                                print("CORRECT")
            active_player = switch_turn(player2)
            end_of_round = True


def switch_turn(player):
    if player == player1:
        player = player2
    else:
        player = player1
    return player
