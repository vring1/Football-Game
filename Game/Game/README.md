# Football Game

## E/R Diagram


## Initialization
Clone / download repository files.

In pgAdmin, create a database called 'game'.
Within the created database in pgAdmin, create a schema called 'game'.

Activate the virtual environment using the OS/shell dependent command for utils/activate
    Using the bash shell:
        source utils/activate

    Using Windows cmd
        utils/activate.bat

Run the following command to install the necessary packages: (could be done in a virtual environment)

    pip install -r requirements.txt

The .env file should be as the following:

    SECRET_KEY=<secret_key>
    DB_USERNAME=postgres || <postgres_user_name>
    DB_PASSWORD=postgres || <postgres_user_password>
    DB_NAME=game || <postgres_db_name>

To initialize the database run the following commands.

    cd utils
    python init_db.py

Now that everything has been set up, you can run it.
    
    flask run


## Interaction with website and game rules
The design is very minimalistic, and should be straight forward. 

### Game rules
The purpose of the game, is that two users compete against eachother in a footballplayer guessing game.

The game is turn-based. Firstly User1 should input and submit the name of a player, who has played for User1's assigned country and club.

Then User2 should input and submit the name of a player, who has played for User2's assigned country and club.

The assigned countries are used the whole game. After each round, the users get a new club, which they again should guess a player from, in accordance to the assigned countries.

The first user to guess right in a round, where the other user guesses wrong, is the winner.

If you are having trouble guessing the correct player, please use 'players_careers.txt' as cheatsheet.


## Backend issues
A game is only set as completed when a new game is started. This could create problems: if the user opens another browser, they could keep playing a game, which should be completed.


## Frontend issues
We did not prioritize creating a beautiful webpage. Our CSS styling is absolute, which can problematic when viewed on displays on different sizes. This would, had we prioritized this more, be fixed by using flexboxes.







