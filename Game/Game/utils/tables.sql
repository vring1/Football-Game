DROP TABLE IF EXISTS game.User CASCADE;

CREATE TABLE IF NOT EXISTS game.User(
	id integer not null,
	playing_as integer,
	name varchar(50) UNIQUE,
	--password varchar(120),
    CONSTRAINT User_pkey PRIMARY KEY (id)
);

DROP TABLE IF EXISTS game.Country CASCADE;

CREATE TABLE IF NOT EXISTS game.Country(
	id integer not null,
	name varchar(50) UNIQUE,
    CONSTRAINT Country_pkey PRIMARY KEY (id)
);

DROP TABLE IF EXISTS game.Player CASCADE;

CREATE TABLE IF NOT EXISTS game.Player(
	id integer not null,
	full_name varchar(50) UNIQUE,
	country_id integer NOT NULL,
    CONSTRAINT Player_pkey PRIMARY KEY (id),
	    CONSTRAINT player_country_fk FOREIGN KEY (country_id)
        REFERENCES game.Country (id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

DROP TABLE IF EXISTS game.Club CASCADE;

CREATE TABLE IF NOT EXISTS game.Club(
	id integer not null,
	name varchar(50) UNIQUE,
    CONSTRAINT Club_pkey PRIMARY KEY (id)
);

DROP TABLE IF EXISTS game.PlayerHasPlayedInClub CASCADE;

CREATE TABLE IF NOT EXISTS game.PlayerHasPlayedInClub(
	id integer not null,
	player_id integer NOT NULL,
	club_id integer NOT NULL,
    CONSTRAINT PlayerHasPlayedInClub_pkey PRIMARY KEY (id),
	CONSTRAINT playerInClub_Player_fk FOREIGN KEY (player_id)
	REFERENCES game.Player(id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT playerInClub_Club_fk FOREIGN KEY (club_id)
	REFERENCES game.Club (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION
);

DROP TABLE IF EXISTS game.Game CASCADE;

CREATE TABLE IF NOT EXISTS game.Game(
	id integer not null,
	user1_id integer NOT NULL,
	user2_id integer NOT NULL,
	user1_country_id integer NOT NULL,
	user2_country_id integer NOT NULL,
	game_status varchar(20) NOT NULL,
    CONSTRAINT Game_pkey PRIMARY KEY (id),
	CONSTRAINT Game_User1_fk FOREIGN KEY (user1_id)
	REFERENCES game.User (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT Game_User2_fk FOREIGN KEY (user2_id)
	REFERENCES game.User (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT Game_User1_Country_fk FOREIGN KEY (user1_country_id)
	REFERENCES game.Country (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT Game_User2_Country_fk FOREIGN KEY (user2_country_id)
	REFERENCES game.Country (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION
);

DROP TABLE IF EXISTS game.GameRound CASCADE;

CREATE TABLE IF NOT EXISTS game.GameRound (
	id integer not null,
	round integer NOT NULL,
	game_id integer NOT NULL,
	user1_club_id integer NOT NULL,
	user1_player_guess varchar(50),
	user1_correct boolean,
	user2_club_id integer NOT NULL,
	user2_player_guess varchar(50),
	user2_correct boolean,
	game_round_status varchar(20) NOT NULL,
    CONSTRAINT GameRound_pkey PRIMARY KEY (id),
	CONSTRAINT GameRound_Game_fk FOREIGN KEY (game_id)
	REFERENCES game.Game(id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT GameRound_Club1_fk FOREIGN KEY (user1_club_id)
	REFERENCES game.Club(id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT GameRound_Club2_fk FOREIGN KEY (user2_club_id)
	REFERENCES game.Club(id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION
);

DROP TABLE IF EXISTS game.GameStatistics CASCADE;

CREATE TABLE IF NOT EXISTS game.GameStatistics(
	id integer not null,
	winner_user_id integer NOT NULL,
	loser_user_id integer NOT NULL,
	game_played timestamp NOT NULL,
    CONSTRAINT GameStats_pkey PRIMARY KEY (id),
	CONSTRAINT GameStats_Winner_User_fk FOREIGN KEY (winner_user_id)
	REFERENCES game.User (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION,
	CONSTRAINT GameStats_Loser_User_fk FOREIGN KEY (loser_user_id)
	REFERENCES game.User (id) MATCH SIMPLE
	ON UPDATE NO ACTION
	ON DELETE NO ACTION
);

-- View for game
CREATE OR REPLACE VIEW game.ViewGame AS
  SELECT 
  	ga.id game_id,
	ga.user1_id,
	us1.name user1_name,
	ga.user2_id,
	us2.name user2_name,
	ga.user1_country_id,
	co1.name country1_name,
	ga.user2_country_id,
	co2.name country2_name,
	ga.game_status
  FROM game.Game ga
  JOIN game.User us1 ON ga.user1_id = us1.id
  JOIN game.User us2 ON ga.user2_id = us2.id
  JOIN game.Country co1 ON ga.user1_country_id = co1.id
  JOIN game.Country co2 ON ga.user2_country_id = co2.id
;

-- View for game round
CREATE OR REPLACE VIEW game.ViewGameRound AS
  SELECT
	gr.id,
	gr.round,
	gr.game_id,
	gr.user1_club_id,
	cl1.name user1_club_name,
	gr.user1_player_guess,
	gr.user1_correct,
	gr.user2_club_id,
	cl2.name user2_club_name,
	gr.user2_player_guess,
	gr.user2_correct,
	gr.game_round_status
  FROM game.GameRound gr
  JOIN game.Club cl1 on (cl1.id = gr.user1_club_id)
  JOIN game.Club cl2 on (cl2.id = gr.user2_club_id)
;

-- View for all players in clubs
CREATE OR REPLACE VIEW game.ViewPlayersInClubs AS
  SELECT pl.id player_id, 
  	pl.full_name full_name,
	co.id country_id, 
	co.name country_name, 
	cl.id club_id,
	cl.name club_name
  FROM game.Player pl
  JOIN game.PlayerHasPlayedInClub pic ON pic.player_id = pl.id
  JOIN game.Club cl ON cl.id = pic.club_id
  JOIN game.Country co ON co.id = pl.country_id
;

