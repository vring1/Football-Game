
player1 = "john" #get user by name or id
player2 = "ali"

def play_game():

    active_player = player1

    #først får player1 og player2 tildelt sig et land hver, som de skal gætte spillere fra
    player1_country = "danmark" #get a random country
    player2_country = "tyskland"
    
    #lav en liste med spillere fra danmark og tyskland, der kan bruges
    players_from_player1_country = ["CHRISTIAN ERIKSEN", "SIMON KJÆR", "KASPER SCHMEICHEL", "DANIEL AGGER", "MIKKEL DAMSGAARD"]
    players_from_player2_country = ["MANUEL NEUER", "JEROME BOATENG", "MATS HUMMELS", "SEBASTIAN SCHWEINSTEIGER", "KAI HAVERTZ"]

    #the players and their clubs
    christian_eriksen_clubs = ["AJAX", "MANCHESTER UNITED", "TOTTENHAM"] #brug playerhasplayedinclub til at vise Ajax, men ikke spilleren.
    manuel_neuer_clubs = ["BAYERN MUNICH", "SCHALKE 04"]

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
            #nu får player1 sin først klub at vide:
            player1_club = "AJAX" #brug playerhasplayedinclub til at vise Ajax, men ikke spilleren.

            print(player1,", choose a player from", player1_country, ", which has played in",player1_club)
            player1_guess = input().upper()

            #check om player1 har gættet på en fra det rigtige land
            if player1_guess in players_from_player1_country:
                if player1_club in christian_eriksen_clubs:
                    player1_guessed_right = True #tjek om spilleren også har en relation til det rigtige hold (DEN SKAL GENERALISERES)
                    print("CORRECT")
                else:
                    player1_guessed_right = False
                    print("PLAYER DOES NOT PLAY IN THE CLUB")
            else:
                player1_guessed_right = False
                print("PLAYER IS NOT FROM THE COUNTRY")
            active_player = switch_turn(player1)

        if active_player == player2:
            player2_club = "BAYERN MUNICH"
            print(player2,", choose a player from", player2_country, ", which has played in",player2_club)
            player2_guess = input().upper()    

            #check om player2 har gættet på en fra det rigtige land
            if player2_guess in players_from_player2_country:
                if player2_club in manuel_neuer_clubs:
                    player2_guessed_right = True #tjek om spilleren også har en relation til det rigtige hold (DEN SKAL GENERALISERES)
                    print("CORRECT")
                else:
                    player2_guessed_right = False
                    print("PLAYER DOES NOT PLAY IN THE CLUB")
            else:
                player2_guessed_right = False
                print("PLAYER IS NOT FROM THE COUNTRY")
            active_player = switch_turn(player2)
            end_of_round = True

def switch_turn(player):
    if player == player1:
        player = player2
    else:
        player = player1
    return player


play_game()
