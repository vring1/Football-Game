import psycopg2
from config import config
#the cursor and the connection is the communication between python and the database.

#connection = psycopg2.connect(host="localhost", port="5432",database="GreenGroceries", user="postgres", password="postgres")
def connect():
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params) #extract everything within params

        # create cursor
        cursor = connection.cursor()
        print('PostgreSQL database version: ')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

if __name__ == "__main__":
    connect()