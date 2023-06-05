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

class Country(ModelMixin):
    def __init__(self, country_data: Dict):
        super(User, self).__init__(country_data)
        self.id = country_data.get('id')
        self.name = country_data.get('name')

class Club(ModelMixin):
    def __init__(self, club_data: Dict):
        super(User, self).__init__(club_data)
        self.id = club_data.get('id')
        self.name = club_data.get('name')

class Game(ModelMixin):
    def __init__(self, game_data: Dict):
        super(User, self).__init__(game_data)
        self.id = game_data.get('id')
        self.user1_id = game_data.get('user1_id')
        self.user2_id = game_data.get('user2_id')
        self.country1_id = game_data.get('country1_id')
        self.country2_id = game_data.get('country2_id')
        self.user1_name = game_data.get('user1_name')
        self.user2_name = game_data.get('user2_name')
        self.country1_name = game_data.get('country1_name')
        self.country2_name = game_data.get('country2_name')
        self.game_status = game_data.get('game_status')

#player
class Player(ModelMixin):
    def __init__(self, player_data: Dict):
        super(User, self).__init__(player_data)
        self.id = player_data.get('name')
        self.name = player_data.get('name')
        self.country_id = player_data.get('country_id')

#playerhasplayedinclub
class PlayerHasPlayedInClub(ModelMixin):
    def __init__(self, playerHasPlayedInClub_data: Dict):
        super(User, self).__init__(playerHasPlayedInClub_data)
        self.id = playerHasPlayedInClub_data.get('id')
        self.player_id = playerHasPlayedInClub_data.get('player_id')
        self.club_id = playerHasPlayedInClub_data.get('club_id')
        self.full_name = playerHasPlayedInClub_data.get('full_name')
        self.country_name = playerHasPlayedInClub_data.get('country_name')
        self.club_name = playerHasPlayedInClub_data.get('club_name')
        self.country_id = playerHasPlayedInClub_data.get('country_id')

class GameRound(ModelMixin):
    def __init__(self, game_round_data: Dict):
        super(User, self).__init__(game_round_data)
        self.id = game_round_data.get('id')
        self.round = game_round_data.get('round')
        self.game_id = game_round_data.get('game_id')
        self.user1_club_id = game_round_data.get('user1_club_id')
        self.user1_club_name = game_round_data.get('user1_club_name')
        self.user1_player_guess = game_round_data.get('user1_player_guess')
        self.user1_correct = game_round_data.get('user1_correct')
        self.user2_club_id = game_round_data.get('user2_club_id')
        self.user2_club_name = game_round_data.get('user2_club_name')
        self.user2_player_guess = game_round_data.get('user2_player_guess')
        self.user2_correct = game_round_data.get('user2_correct')
        self.game_round_status = game_round_data.get('game_round_status')
        
        
        