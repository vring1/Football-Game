DROP TABLE IF EXISTS game.User CASCADE;

CREATE TABLE IF NOT EXISTS game.User(
	id integer not null,
	name varchar(50) UNIQUE,
	password varchar(120),
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

--DROP TABLE IF EXISTS game.UserSelectsPlayer CASCADE;
--
--CREATE TABLE IF NOT EXISTS game.UserSelectsPlayer(
--	id integer not null,
--	user_id integer NOT NULL,
--	player_id integer NOT NULL,
--    CONSTRAINT UserSelectsPlayer_pkey PRIMARY KEY (id),
--	CONSTRAINT UserSelects_User_fk FOREIGN KEY (user_id)
--	REFERENCES game.User (id) MATCH SIMPLE
--	ON UPDATE NO ACTION
--	ON DELETE NO ACTION,
--	CONSTRAINT UserSelects_Player_fk FOREIGN KEY (player_id)
--	REFERENCES game.Player(id) MATCH SIMPLE
--	ON UPDATE NO ACTION
--	ON DELETE NO ACTION
--);

-- View for dictionary
CREATE OR REPLACE VIEW game.ViewPlayersInClubs AS
  SELECT pl.full_name full_name, co.name country, cl.name club
  FROM game.Player pl
  JOIN game.PlayerHasPlayedInClub pic ON pic.player_id = pl.id
  JOIN game.Club cl ON cl.id = pic.club_id
  JOIN game.Country co ON co.id = pl.country_id
;
