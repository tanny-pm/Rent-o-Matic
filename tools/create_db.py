"""
データベース作成用のスクリプト
"""

import sqlite3

conn = sqlite3.connect("rentomatic.db")

cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE room(
        code STRING PRIMARY KEY,
        size INT,
        price INT,
        longitude REAL,
        latitude REAL
    )
    """
)
cur.execute('INSERT INTO room VALUES("1111", 215, 39, -0.09998975, 51.75436293)')
cur.execute('INSERT INTO room VALUES("2222", 405, 66, 0.18228006, 51.74640997)')
cur.execute('INSERT INTO room VALUES("3333",  56, 60, 0.27891577, 51.45994069)')
cur.execute('INSERT INTO room VALUES("4444",  93, 48, 0.33894476, 51.39916678)')
conn.commit()
conn.close()
