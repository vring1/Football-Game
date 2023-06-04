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
        self.name = user_data.get('name')
        self.password = user_data.get('password')
