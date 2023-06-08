# Football Game

## E/R Diagram


## Initialization
Create a database called 'game'.

Create a schema called 'game'.

Instead of creating a venv, just activate the one already created. The only requirement is psycopg2, so we just pushed the venv config also.

The .env file should be as the following:

    SECRET_KEY=<secret_key>
    DB_USERNAME=postgres || <postgres_user_name>
    DB_PASSWORD=postgres || <postgres_user_password>
    DB_NAME=game || <postgres_db_name>

To initialize the database do:

    cd utils
    python init_db.py

Lastly, do:
    
    flask run


## Interaction with website and game rules
The design is very minimalistic, and should be straight forward. 

### Game rules
The purpose of the game, is that two users compete against eachother in a footballplayer guessing game.

The game is turn-based. Firstly User1 should input and submit the name of a player, who has played for User1's assigned country and club.

Then User2 should input and submit the name of a player, who has played for User2's assigned country and club.

The assigned countries are used the whole game. After each round, the users get a new club, which they again should guess a player from, in accordance to the assigned countries.

The first user to guess right in a round, where the other user guesses wrong, is the winner.

Use 'players_carrers.txt' as cheatsheet, if You're having trouble guessing the players.