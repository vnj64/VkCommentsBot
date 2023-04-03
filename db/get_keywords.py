import psycopg2
from db.database import connect
from config import host, password, user, name, port


def get_keywords_list():
    connect()
    keywords = []
    conn = psycopg2.connect(
        host=host,
        password=password,
        user=user,
        dbname=name,
        port=port
    )

    cur = conn.cursor()
    query = "SELECT keyword FROM keywords"
    cur.execute(query)

    lst = cur.fetchall()
    for row in lst:
        keywords.append(row[0])

    return keywords


