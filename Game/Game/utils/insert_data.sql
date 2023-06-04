DELETE FROM game.userselectsplayer;
DELETE FROM game.playerhasplayedinclub;
DELETE FROM game.player;
DELETE FROM game.club;
DELETE FROM game.country;

INSERT INTO game.Country (id, name) VALUES (1, 'Portugal');
INSERT INTO game.Country (id, name) VALUES (2, 'Danmark');
INSERT INTO game.Country (id, name) VALUES (3, 'Frankrig');
INSERT INTO game.Country (id, name) VALUES (4, 'Argentina');

INSERT INTO game.Player(id, full_name, country_id) VALUES (5, 'Cristiano Ronaldo', 1);
INSERT INTO game.Player(id, full_name, country_id) VALUES (6, 'Bernardo Silva', 1);
INSERT INTO game.Player(id, full_name, country_id) VALUES (7, 'Joao Cancelo', 1);
INSERT INTO game.Player(id, full_name, country_id) VALUES (8, 'Christian Eriksen', 2);
INSERT INTO game.Player(id, full_name, country_id) VALUES (9, 'Michael Laudrup', 2);
INSERT INTO game.Player(id, full_name, country_id) VALUES (10, 'Brian Laudrup', 2);
INSERT INTO game.Player(id, full_name, country_id) VALUES (11, 'Lionel Messi', 4);
INSERT INTO game.Player(id, full_name, country_id) VALUES (12, 'Maradona', 4);
INSERT INTO game.Player(id, full_name, country_id) VALUES (13, 'Antoine Griezmann', 3);
INSERT INTO game.Player(id, full_name, country_id) VALUES (14, 'Karim Benzema', 3);
INSERT INTO game.Player(id, full_name, country_id) VALUES (15, 'Olivier Giroud', 3);

INSERT INTO game.club(id, name) VALUES (16, 'AC Milan');
INSERT INTO game.club(id, name) VALUES (17, 'Ajax');
INSERT INTO game.club(id, name) VALUES (18, 'Al Nassr');
INSERT INTO game.club(id, name) VALUES (19, 'Arsenal');
INSERT INTO game.club(id, name) VALUES (20, 'Atletico Madrid');
INSERT INTO game.club(id, name) VALUES (21, 'Barcelona');
INSERT INTO game.club(id, name) VALUES (22, 'Bayern Munchen');
INSERT INTO game.club(id, name) VALUES (23, 'Benfica');
INSERT INTO game.club(id, name) VALUES (24, 'Boca Juniors');
INSERT INTO game.club(id, name) VALUES (25, 'Brentford');
INSERT INTO game.club(id, name) VALUES (26, 'Brøndby IF');
INSERT INTO game.club(id, name) VALUES (27, 'Chelsea');
INSERT INTO game.club(id, name) VALUES (28, 'FC København');
INSERT INTO game.club(id, name) VALUES (29, 'Fiorentina');
INSERT INTO game.club(id, name) VALUES (30, 'Grenoble');
INSERT INTO game.club(id, name) VALUES (31, 'Inter Milan');
INSERT INTO game.club(id, name) VALUES (32, 'Juventus');
INSERT INTO game.club(id, name) VALUES (33, 'Lazio');
INSERT INTO game.club(id, name) VALUES (34, 'Lyon');
INSERT INTO game.club(id, name) VALUES (35, 'Manchester City');
INSERT INTO game.club(id, name) VALUES (36, 'Manchester United');
INSERT INTO game.club(id, name) VALUES (37, 'Monaco');
INSERT INTO game.club(id, name) VALUES (38, 'Montpellier');
INSERT INTO game.club(id, name) VALUES (39, 'Napoli');
INSERT INTO game.club(id, name) VALUES (40, 'Paris Saint Germain');
INSERT INTO game.club(id, name) VALUES (41, 'Rangers FC');
INSERT INTO game.club(id, name) VALUES (42, 'Real Madrid');
INSERT INTO game.club(id, name) VALUES (43, 'Real Sociedad');
INSERT INTO game.club(id, name) VALUES (44, 'Sevilla');
INSERT INTO game.club(id, name) VALUES (45, 'Sporting CP');
INSERT INTO game.club(id, name) VALUES (46, 'Tottenham');
INSERT INTO game.club(id, name) VALUES (47, 'Valencia');
INSERT INTO game.club(id, name) VALUES (48, 'Vissel Kobe');

INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (49, 5, 45);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (50, 5, 36);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (51, 5, 42);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (52, 5, 32);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (53, 5, 18);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (54, 6, 23);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (55, 6, 37);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (56, 6, 35);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (57, 7, 23);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (58, 7, 47);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (59, 7, 31);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (60, 7, 32);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (61, 7, 35);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (62, 7, 22);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (63, 8, 17);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (64, 8, 46);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (65, 8, 31);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (66, 8, 25);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (67, 8, 36);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (68, 9, 26);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (69, 9, 33);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (70, 9, 32);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (71, 9, 21);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (72, 9, 42);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (73, 9, 48);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (74, 9, 17);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (75, 10, 26);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (76, 10, 22);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (77, 10, 29);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (78, 10, 16);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (79, 10, 41);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (80, 10, 27);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (81, 10, 28);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (82, 10, 17);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (83, 11, 21);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (84, 11, 40);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (85, 12, 24);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (86, 12, 21);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (87, 12, 39);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (88, 12, 44);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (89, 13, 43);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (90, 13, 20);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (91, 13, 21);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (92, 14, 34);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (93, 14, 42);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (94, 15, 30);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (95, 15, 38);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (96, 15, 19);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (97, 15, 27);
INSERT INTO game.playerhasplayedinclub(id, player_id, club_id) VALUES (98, 15, 16);

drop SEQUENCE IF EXISTS game.id_seq;

CREATE SEQUENCE game.id_seq
INCREMENT 1
START 100;


-- Check data
SELECT *
FROM game.Player pl
JOIN game.PlayerHasPlayedInClub pic ON pic.player_id = pl.id
JOIN game.Club cl ON cl.id = pic.club_id
JOIN game.Country co ON (co.id = pl.country_id)
;

SELECT * FROM game.ViewPlayersInClubs;
