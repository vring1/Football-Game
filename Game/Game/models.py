from Game import login_manager


@login_manager.user_loader


class Country(tuple):
    def __init__(self, country_data):
        self.id = country_data[0]
        self.name = country_data[1]

class Game(tuple):
    def __init__(self, game_data):
        self.id = game_data[0]
        self.user1_id = game_data[1]
        self.user1_name = game_data[2]
        self.user2_id = game_data[3]
        self.user2_name = game_data[4]
        self.country1_id = game_data[5]
        self.country1_name = game_data[6]
        self.country2_id = game_data[7]
        self.country2_name = game_data[8]
        self.game_status = game_data[9]

class PlayerHasPlayedInClub(tuple): #VIEW!
    def __init__(self, playerHasPlayedInClub_data):
        self.player_id = playerHasPlayedInClub_data[0]
        self.full_name = playerHasPlayedInClub_data[1]
        self.country_id = playerHasPlayedInClub_data[2]
        self.country_name = playerHasPlayedInClub_data[3]
        self.club_id = playerHasPlayedInClub_data[4]
        self.club_name = playerHasPlayedInClub_data[5]

class GameRound(tuple): #VIEW!
    def __init__(self, game_round_data):
        self.id = game_round_data[0]
        self.round_number = game_round_data[1]
        self.game_id = game_round_data[2]
        self.user1_club_id = game_round_data[3]
        self.user1_club_name = game_round_data[4]
        self.user1_player_guess = game_round_data[5]
        self.user1_correct = game_round_data[6]
        self.user2_club_id = game_round_data[7]
        self.user2_club_name = game_round_data[8]
        self.user2_player_guess = game_round_data[9]
        self.user2_correct = game_round_data[10]
        self.game_round_status = game_round_data[11]
    