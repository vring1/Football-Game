from Game import conn
from Game.models import PlayerHasPlayedInClub, Country, Game, GameRound


# INSERT QUERIES
#def insert_user(user: User):
#    cur = conn.cursor()
#    sql = """
#    INSERT INTO game.User(id, name, password)
#    VALUES (nextval('game.id_seq'), %s, %s)
#    """
#    cur.execute(sql, (user.name, user.password))
#    conn.commit()
#    cur.close()

   
#def insert_user_selects_player(id, user_id, player_id):
#    cur = conn.cursor()
#    sql = """
#    INSERT INTO game.UserSelectsPlayer(id, user_id, player_id)
#    VALUES (%s, %s, %s)
#    """
#    cur.execute(sql, (id, user_id, player_id))
#    conn.commit()
#    cur.close()


def insert_game(user1_id, user2_id, user1_country_id, user2_country_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO game.Game(id, user1_id, user2_id, user1_country_id, user2_country_id, game_status)
    VALUES (nextval('game.id_seq'), %s, %s, %s, %s, 'STARTED')
    """
    cur.execute(sql, (user1_id, user2_id, user1_country_id, user2_country_id))
    conn.commit()
    cur.close()


def insert_game_round(round_number, game_id, user1_club_id, user2_club_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO game.GameRound(id, round_number, game_id, user1_club_id, user2_club_id, game_round_status)
    VALUES (nextval('game.id_seq'), %s, %s, %s, %s, 'STARTED')
    """
    cur.execute(sql, (round_number, game_id, user1_club_id, user2_club_id))
    conn.commit()
    cur.close()


# SELECT QUERIES
#def get_user_by_name(name):
#    cur = conn.cursor()
#    sql = """
#    SELECT * FROM game.User
#    WHERE name = %s
#    """
#    cur.execute(sql, (name,))
#    user = User(cur.fetchone()) if cur.rowcount > 0 else None
#    cur.close()
#    return user

# Get next sequence number
#def get_next_seqeuence_id():
#    cur = conn.cursor()
#    sql = """
#    SELECT nextval('game.id_seq')
#    """
#    cur.execute(sql)
#    id = int(cur.fetchone()) if cur.rowcount > 0 else None
#    cur.close()
#    return id

# Skal bruges når det indtastede spillernavn skal slåes op.
#def get_player_by_name(name):
#    cur = conn.cursor()
#    sql = """
#    SELECT * FROM game.Player p
#    WHERE UPPER(p.name) = UPPER(%s)
#    """
#    cur.execute(sql, (name,))
#    player = Player(cur.fetchone()) if cur.rowcount > 0 else None
#    cur.close()
#    return player


def get_all_countries():
    cur = conn.cursor()
    sql = """
    SELECT id, name
    FROM game.Country
    ORDER BY name
    """
    cur.execute(sql)
    country = [Country(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
    cur.close()
    return country


#def get_all_clubs():
#    cur = conn.cursor()
#    sql = """
#    SELECT id, name
#    FROM game.Club
#    ORDER BY name
#    """
#    cur.execute(sql)
#    club = [Club(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
#    cur.close()
#    return club


#def get_all_clubs_by_player_name(player_name): #BRUG DENNE TIL AT CHEKKE PÅ INPUT I STRINGFIELD. CHECK MED club_id i ViewGameRound.
#    cur = conn.cursor()
#    sql = """
#    SELECT player_id, full_name, country_id, country_name, club_id, club_name
#    FROM game.ViewPlayersInClubs
#    WHERE player_name = %s    
#    """
#    cur.execute(sql, (player_name,))
#    playerHasPlayedInClub = [PlayerHasPlayedInClub(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
#    cur.close()
#    return playerHasPlayedInClub


def get_played_by_player_name_and_country_id_and_club_id(player_name, country_id, club_id): #BRUG DENNE TIL AT CHEKKE PÅ INPUT I STRINGFIELD. CHECK MED club_id i ViewGameRound.
    cur = conn.cursor()
    sql = """
    SELECT player_id, full_name, country_id, country_name, club_id, club_name
    FROM game.ViewPlayersInClubs
    WHERE full_name = %s
      AND country_id = %s    
      AND club_id = %s
    """
    cur.execute(sql, (player_name, country_id, club_id,))
    playerHasPlayedInClub = [PlayerHasPlayedInClub(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
    cur.close()
    return playerHasPlayedInClub


def get_all_clubs_by_country_id(game_id, country_id, username):
    cur = conn.cursor()
    sql = """
    SELECT pc.player_id, pc.full_name, pc.country_id, pc.country_name, pc.club_id, pc.club_name
    FROM game.ViewPlayersInClubs pc
    WHERE pc.country_id = %s
    AND NOT EXISTS (SELECT 'x'
                    FROM game.GameRound gr
                    WHERE gr.game_id = %s
                      AND (('User1' = %s AND gr.user1_club_id = pc.club_id) OR
                           ('User2' = %s AND gr.user2_club_id = pc.club_id))
                    )
    """
    cur.execute(sql, (country_id, game_id, username, username,))
    playerHasPlayedInClub = [PlayerHasPlayedInClub(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
    cur.close()
    return playerHasPlayedInClub


def get_game_by_status(game_status):
    cur = conn.cursor()
    sql = """
    SELECT 
        game_id,
        user1_id,
        user1_name,
        user2_id,
        user2_name,
        user1_country_id,
        country1_name,
        user2_country_id,
        country2_name,
        game_status
    FROM game.ViewGame
    WHERE game_status = %s
    """
    cur.execute(sql, (game_status,))
    game = Game(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return game

def get_latest_round(game_id):
    cur = conn.cursor()
    sql = """
    SELECT 
      gr.id,
	  gr.round_number,
	  gr.game_id,
	  gr.user1_club_id,
	  gr.user1_club_name,
	  gr.user1_player_guess,
	  gr.user1_correct,
	  gr.user2_club_id,
	  gr.user2_club_name,
	  gr.user2_player_guess,
	  gr.user2_correct,
	  gr.game_round_status
    FROM game.ViewGameRound gr
    where game_id = %s
    and round_number = (select max(r.round_number)
			  from game.ViewGameRound r
			  where r.game_id = %s)
    """
    cur.execute(sql, (game_id,game_id))
    game_round = GameRound(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return game_round

def get_all_rounds(game_id):
    cur = conn.cursor()
    sql = """
    SELECT 
      gr.id,
	  gr.round_number,
	  gr.game_id,
	  gr.user1_club_id,
	  gr.user1_club_name,
	  gr.user1_player_guess,
	  gr.user1_correct,
	  gr.user2_club_id,
	  gr.user2_club_name,
	  gr.user2_player_guess,
	  gr.user2_correct,
	  gr.game_round_status
    FROM game.ViewGameRound gr
    WHERE gr.game_id = %s
    ORDER BY gr.round_number 
    """
    cur.execute(sql, (game_id,))
    game_round = [GameRound(res) for res in cur.fetchall()] if cur.rowcount > 0 else []
    cur.close()
    return game_round


# UPDATE QUERIES
#def update_user(id, playing_as):
#    cur = conn.cursor()
#    sql = """
#    UPDATE game.user
#    SET playing_as = %s
#    WHERE id = %s
#    """
#    cur.execute(sql, (id, playing_as))
#    conn.commit()
#    cur.close()


def update_game_round(round_number, game_id, user1_player_guess, user1_correct, user2_player_guess, user2_correct, game_round_status):
    cur = conn.cursor()
    sql = """
    UPDATE game.GameRound
    SET user1_player_guess = %s,
        user1_correct = %s,
        user2_player_guess = %s,
        user2_correct = %s,
        game_round_status = %s
    WHERE round_number = %s
      AND game_id = %s
    """
    cur.execute(sql, (user1_player_guess, user1_correct, user2_player_guess, user2_correct, game_round_status, round_number, game_id,))
    conn.commit()
    cur.close()


# Overvej evt. også en simplere update, som kun bruges til at opdatere has_won, guessed_right, no_of_wins.
def complete_game(id):
    cur = conn.cursor()
    sql = """
    UPDATE game.Game
    SET game_status = 'COMPLETED'
    WHERE id = %s
    """
    cur.execute(sql, (id,))
    conn.commit()
    cur.close()
