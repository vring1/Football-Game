from Game import db_cursor, conn
from Game.models import User, Player, PlayerHasPlayedInClub, Club, Country


# INSERT QUERIES
def insert_user(user: User):
    sql = """
    INSERT INTO game.User(id, name, password)
    VALUES (nextval('game.id_seq'), %s, %s)
    """
    db_cursor.execute(sql, (user.name, user.password))
    conn.commit()


def insert_user_selects_player(id, user_id, player_id):
    sql = """
    INSERT INTO game.UserSelectsPlayer(id, user_id, player_id)
    VALUES (%s, %s, %s)
    """
    db_cursor.execute(sql, (id, user_id, player_id))
    conn.commit()


# SELECT QUERIES
def get_user_by_name(name):
    sql = """
    SELECT * FROM game.User
    WHERE name = %s
    """
    db_cursor.execute(sql, (name,))
    user = User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return user


# Skal bruges når det indtastede spillernavn skal slåes op.
def get_player_by_name(name):
    sql = """
    SELECT * FROM game.Player p
    WHERE UPPER(p.name) = UPPER(%s)
    """
    db_cursor.execute(sql, (name,))
    player = Player(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return player


def get_all_countries():
    sql = """
    SELECT id, name
    FROM game.Country
    ORDER BY name
    """
    db_cursor.execute(sql)
    country = [Country(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return country


def get_all_clubs():
    sql = """
    SELECT id, name
    FROM game.Club
    ORDER BY name
    """
    db_cursor.execute(sql)
    club = [Club(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return club


def get_all_clubs_by_player_id(id):
    sql = """
    SELECT pl.id player_id, pl.full_name, cl.id club_id, cl.name club_name
    FROM game.Player pl
    JOIN game.PlayerHasPlayedInClub pic ON pic.player_id = pl.id
    JOIN game.Club cl ON cl.id = pic.club_id
    WHERE pl.id = %s    
    """
    db_cursor.execute(sql, (id,))
    club = [Club(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return club


# UPDATE QUERIES
# Slet denne queriy hvis vi ikke skal opdatere win/guess/no-of-wins
# def update_user(id, name, password, has_won, guessed_right, no_of_wins):
#     sql = """
#     UPDATE game.User
#     SET name = %s
#         ,password = %s
#         ,has_won = %s
#         ,guessed_right = %s
#         ,no_of_wins = %s
#     WHERE id = %s
#     """
#     db_cursor.execute(sql, (id, name, password, has_won, guessed_right, no_of_wins))
#     conn.commit()

# Overvej evt. også en simplere update, som kun bruges til at opdatere has_won, guessed_right, no_of_wins.


# Bruges, når et nyt spil skal starte.
def delete_user_selects_player():
    sql = """
    DELETE FROM game.UserSelectsPlayer
    """
    db_cursor.execute(sql)
    conn.commit()
