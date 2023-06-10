import psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect("dbname=game user=postgres password=postgres host=localhost")
    with conn.cursor() as cur:
        # Run tables.sql
        with open('tables.sql') as db_file:
            cur.execute(db_file.read())

        # Run insert_data.sql
        with open('insert_data.sql') as db_file:
            cur.execute(db_file.read())

        conn.commit()

    conn.close()
