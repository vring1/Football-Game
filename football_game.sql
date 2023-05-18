-- Drop tables before create
-- Drop intersection tables first because of foreign key constraints
DROP TABLE IF EXISTS game."Player_in_club";
DROP TABLE IF EXISTS game."Player_is_from";
DROP TABLE IF EXISTS game."User";
DROP TABLE IF EXISTS game."Club";
DROP TABLE IF EXISTS game."Country";
DROP TABLE IF EXISTS game."Player";


-- Table: game.Club


CREATE TABLE IF NOT EXISTS game."Club"
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Club_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."Club"
    OWNER to postgres;
	
	
-- Table: game.Country


CREATE TABLE IF NOT EXISTS game."Country"
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Country_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."Country"
    OWNER to postgres;


-- Table: game.Player


CREATE TABLE IF NOT EXISTS game."Player"
(
    id integer NOT NULL,
    full_name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Player_pk" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."Player"
    OWNER to postgres;


-- Table: game.Player_in_club

CREATE TABLE IF NOT EXISTS game."Player_in_club"
(
    id integer NOT NULL,
    player_id integer NOT NULL,
    club_id integer NOT NULL,
    CONSTRAINT "Player_in_club_pkey" PRIMARY KEY (id),
    CONSTRAINT club_fk FOREIGN KEY (club_id)
        REFERENCES game."Club" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT player_fk FOREIGN KEY (player_id)
        REFERENCES game."Player" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."Player_in_club"
    OWNER to postgres;
-- Index: fki_club_fk

DROP INDEX IF EXISTS game.fki_club_fk;

CREATE INDEX IF NOT EXISTS fki_club_fk
    ON game."Player_in_club" USING btree
    (club_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_player_fk

DROP INDEX IF EXISTS game.fki_player_fk;

CREATE INDEX IF NOT EXISTS fki_player_fk
    ON game."Player_in_club" USING btree
    (player_id ASC NULLS LAST)
    TABLESPACE pg_default;


-- Table: game.Player_is_from

CREATE TABLE IF NOT EXISTS game."Player_is_from"
(
    id integer NOT NULL,
    player_id integer NOT NULL,
    country_id integer NOT NULL,
    CONSTRAINT "Player_is_from_pkey" PRIMARY KEY (id),
    CONSTRAINT pifc_country_fk FOREIGN KEY (country_id)
        REFERENCES game."Country" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT pifc_player_fk FOREIGN KEY (player_id)
        REFERENCES game."Player" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."Player_is_from"
    OWNER to postgres;
-- Index: fki_i

DROP INDEX IF EXISTS game.fki_i;

CREATE INDEX IF NOT EXISTS fki_i
    ON game."Player_is_from" USING btree
    (player_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_pifc_country_fk

-- DROP INDEX IF EXISTS game.fki_pifc_country_fk;

CREATE INDEX IF NOT EXISTS fki_pifc_country_fk
    ON game."Player_is_from" USING btree
    (country_id ASC NULLS LAST)
    TABLESPACE pg_default;


-- Table: game.User


CREATE TABLE IF NOT EXISTS game."User"
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    has_won boolean NOT NULL DEFAULT false,
    guessed_right boolean,
    no_of_wins integer NOT NULL DEFAULT 0,
    CONSTRAINT "User_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS game."User"
    OWNER to postgres;

	
	
delete from game."Player_in_club";
delete from game."Player";
delete from game."Club";

INSERT INTO game."Player"(id, full_name) VALUES (1, 'Ronaldo');
INSERT INTO game."Player"(id, full_name) VALUES (2, 'Messi');

INSERT INTO game."Club"(id, name) VALUES (2, 'Real Madrid');
INSERT INTO game."Club"(id, name) VALUES (3, 'Barcelona');

INSERT INTO game."Player_in_club"(id, player_id, club_id) VALUES (1, 1, 2);
INSERT INTO game."Player_in_club"(id, player_id, club_id) VALUES (2, 2, 3);
	
select * from game."Club";

select * from game."Player";

select * from game."Player_in_club";

select *
from game."Player_in_club" pc
join game."Club" c ON c.id = pc.club_id
join game."Player" p ON p.id = pc.player_id

