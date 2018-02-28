import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None

    params = config()

    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    print(conn)

    cur = conn.cursor()
    print(cur)

    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)

    cur.close()
    if conn is not None:
        conn.close()
        print('Database connection closed.')

connect()