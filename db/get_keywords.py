import psycopg2
from db.database import connect
from config import load_config

config = load_config('.env')


def get_keywords_list():
    connect()
    keywords = []
    conn = psycopg2.connect(
        host=config.db.host,
        password=config.db.password,
        user=config.db.user,
        dbname=config.db.database,
        port=config.db.port
    )

    cur = conn.cursor()
    query = "SELECT keyword FROM keywords"
    cur.execute(query)

    lst = cur.fetchall()
    for row in lst:
        keywords.append(row[0])

    return keywords


def add_keyword_db(keyword):
    conn = psycopg2.connect(
        host=config.db.host,
        password=config.db.password,
        user=config.db.user,
        dbname=config.db.database,
        port=config.db.port
    )
    cur = conn.cursor()
    query = f'INSERT INTO keywords (keyword) VALUES "{keyword}"'
    cur.execute(query)
