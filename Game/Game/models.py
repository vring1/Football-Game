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
        self.id = user_data.get('id')
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


