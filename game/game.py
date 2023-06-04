import psycopg2
import os
import random

player1 = "john"  # get user by name or id
player2 = "ali"


def play_game():
    conn = psycopg2.connect("dbname=game user=postgres password=postgres host=localhost")

    # Dictionary for player, country and clubs
    with conn.cursor() as cur:
        # extract a player list from db
        cur.execute("SELECT UPPER(full_name), country, STRING_AGG(club, ',') FROM game.viewplayersinclubs GROUP BY UPPER(full_name), country")
        result_set = cur.fetchall()
        players = {row[0]: [row[1], row[2].split(',')] for row in result_set}
        print("Dict: ", players)
    conn.close()

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


play_game()
