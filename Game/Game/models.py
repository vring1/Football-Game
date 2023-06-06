from typing import Dict

from flask_login import UserMixin
from psycopg2 import sql

from Game import login_manager, db_cursor, conn, app


@login_manager.user_loader
def load_user(id):
    user_sql = sql.SQL("""
    SELECT * FROM game.User
    WHERE id = %s
    """).format(sql.Identifier('id'))

    db_cursor.execute(user_sql, (id,))
    return User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None


class ModelUserMixin(dict, UserMixin):
    @property
    def id(self):
        return self.id


class ModelMixin(dict):
    pass


class User(ModelUserMixin):
    def __init__(self, user_data: Dict):
        super(User, self).__init__(user_data)
# self.id = user_data.get('id') SKAL IKKE MED DA DEN SÆTTES I SQL MED SEQUENCE: nextval('idseq')
        #self.id = user_data.get('id')
        self.name = user_data.get('name')
        self.password = user_data.get('password')

class Country(tuple):
    def __init__(self, country_data):
        #super(User, self).__init__(country_data)
        self.id = country_data[0]
        self.name = country_data[1]

class Club(tuple):
    def __init__(self, club_data):
        #super(User, self).__init__(club_data)
        self.id = club_data[0]
        self.name = club_data[1]

class Game(tuple):
    def __init__(self, game_data):
        #super(User, self).__init__(game_data)
        self.id = game_data[0]
        self.user1_id = game_data[1]
        self.user2_id = game_data[2]
        self.country1_id = game_data[3]
        self.country2_id = game_data[4]
        self.user1_name = game_data[5]
        self.user2_name = game_data[6]
        self.country1_name = game_data[7]
        self.country2_name = game_data[8]
        self.game_status = game_data[9]

#player
class Player(tuple):
    def __init__(self, player_data):
        #super(User, self).__init__(player_data)
        self.id = player_data[0]
        self.name = player_data[1]
        self.country_id = player_data[2]

#playerhasplayedinclub
class PlayerHasPlayedInClub(tuple): #VIEW
    def __init__(self, playerHasPlayedInClub_data):
        #super(User, self).__init__(playerHasPlayedInClub_data)
        #self.id = playerHasPlayedInClub_data[0]
        self.player_id = playerHasPlayedInClub_data[0]
        self.full_name = playerHasPlayedInClub_data[1]
        self.country_id = playerHasPlayedInClub_data[2]
        self.country_name = playerHasPlayedInClub_data[3]
        self.club_id = playerHasPlayedInClub_data[4]
        self.club_name = playerHasPlayedInClub_data[5]

class GameRound(tuple): #VIEW!
    def __init__(self, game_round_data):
        #super(User, self).__init__(game_round_data)
        self.id = game_round_data[0] # DENNE SKAL MÅSKE IKKE UDKOMMENTERES!!!!!!
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
    