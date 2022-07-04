import sqlite3


def add_parrot_type(img_path):
    cur.execute(f'INSERT INTO parrots_types(image) VALUES ("{img_path}")')
    conn.commit()


def add_parrot(name='Parrot', age=0, owner=0, type=0):
    cur.execute(f'INSERT INTO parrots(name, age, owner, type) VALUES ("{name}", "{age}", "{owner}", "{type}")')
    conn.commit()


def add_user(name, id):
    cur.execute(f'INSERT INTO users(id, username) VALUES("{id}", "@{name}")')
    conn.commit()


conn = sqlite3.connect('../DB/Parrot_Bot.db')
cur = conn.cursor()



