from Game import db_cursor, conn
from Game.models import User, Player, PlayerHasPlayedInClub, Club, Country, Game


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

def insert_game(user1_id, user2_id, user1_country_id, user2_country_id):
    sql = """
    INSERT INTO game.Game(id, user1_id, user2_id, user1_country_id, user2_country_id, game_status)
    VALUES (nextval('game.id_seq'), %s, %s, %s, %s, 'STARTED')
    """
    db_cursor.execute(sql, (user1_id, user2_id, user1_country_id, user2_country_id))
    conn.commit()

def insert_game_round(round, game_id, user1_club_id, user2_club_id):
    sql = """
    INSERT INTO game.GameRound(id, round, game_id, user1_club_id, user2_club_id, game_round_status)
    VALUES (nextval('game.id_seq'), %s, %s, %s, %s, 'STARTED')
    """
    db_cursor.execute(sql, (round, game_id, user1_club_id, user2_club_id))
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

# Get next sequence number
def get_next_seqeuence_id():
    sql = """
    SELECT nextval('game.id_seq')
    """
    db_cursor.execute(sql)
    id = int(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return id

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

def get_all_clubs_by_country_id(country_id):
    sql = """
    SELECT id, player_id, country_id, club_id, full_name, country_name, club_name
    FROM game.PlayerHasPlayedInClub
    WHERE country_id = %s    
    """
    db_cursor.execute(sql, (country_id))
    playerHasPlayedInClub = [PlayerHasPlayedInClub(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return playerHasPlayedInClub

def get_game_by_status(game_status):
    sql = """
    SELECT * FROM game.ViewGame
    WHERE game_status = %s
    """
    db_cursor.execute(sql, (game_status,))
    game = Game(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return game

def get_latest_round(game_id):
    sql = """
    SELECT * FROM game.gameround gr
    where game_id = %s
    and round = (select max(r.round)
			  from game.gameround r
			  where r.game_id = %s)
    """
    db_cursor.execute(sql, (game_id,game_id))
    game = Game(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return game


# UPDATE QUERIES
def update_user(id, playing_as):
     sql = """
     UPDATE game.user
     SET playing_as = %s
     WHERE id = %s
     """
     db_cursor.execute(sql, (id, playing_as))
     conn.commit()

def complete_game(id):
     sql = """
     UPDATE game.Game
     SET STATUS = 'COMPLETED'
     WHERE id = %s
     """
     db_cursor.execute(sql, (id,))
     conn.commit()
# Overvej evt. også en simplere update, som kun bruges til at opdatere has_won, guessed_right, no_of_wins.


# Bruges, når et nyt spil skal starte.
def delete_user_selects_player():
    sql = """
    DELETE FROM game.UserSelectsPlayer
    """
    db_cursor.execute(sql)
    conn.commit()
