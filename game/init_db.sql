import psycopg2
import os

from dotenv import load_dotenv
from choices import df

load_dotenv()

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    with conn.cursor() as cur:
        # Run tables.sql
        with open('tables.sql') as db_file:
            cur.execute(db_file.read())

        # Run insert_data.sql
        with open('insert_data.sql') as db_file:
            cur.execute(db_file.read())

        conn.commit()

    conn.close()
