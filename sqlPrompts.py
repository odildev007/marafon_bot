from sqlite3 import Connection

conn = Connection("data.db")
c = conn.cursor()

def add_user(id, name):
    c.execute("INSERT INTO users (id, name, status) VALUES (?, ?, ?)", (id, name, "active"))
    conn.commit()

def add_referal(user_id, reffer_id):
    c.execute("INSERT INTO referals (user_id, reffer_id, status) VALUES (?, ?, 'warm')", (user_id, reffer_id))
    conn.commit()

def change_user_status(user_id, status):
    c.execute("UPDATE users SET status=? WHERE id=?", (status, user_id))
    conn.commit()

def change_referal_status(user_id, status):
    c.execute("UPDATE referals SET status=? WHERE user_id=?", (status, user_id,))
    conn.commit()

def get_user(user_id):
    user_tpl = c.execute("SELECT name, status FROM users WHERE id=?", (user_id, )).fetchone()
    if user_tpl: return {"name": user_tpl[0], "status": user_tpl[1]}

def get_user_referals(user_id):
    data = c.execute("SELECT user_id, status FROM referals WHERE reffer_id=?", (user_id, )).fetchall()
    referals = []
    if data:
        for i in data:
            referals.append({"user_id": i[0], "status": i[1]})
    return referals

def get_users():
    users = []
    data = c.execute("SELECT id, name, status FROM users").fetchall()
    for i in data:
        users.append({"user_id": i[0], "name": i[1], "status": i[2]})
    return users

def check_user_referal(user_id, reffer_id):
    if c.execute("SELECT status FROM referals WHERE user_id=? AND reffer_id=?", (user_id, reffer_id)).fetchone():
        return 1
    elif c.execute("SELECT status FROM referals WHERE user_id=?", (user_id, )).fetchone(): 
        return 2
    return 3

def get_user_reffer_id(user_id):
    data = c.execute("SELECT reffer_id FROM referals WHERE user_id=?", (user_id, )).fetchone()
    if data: return {"reffer_id": data[0]}

def get_post(menu_name):
    data = c.execute("SELECT img, caption FROM posts WHERE menu_name = ?", (menu_name, )).fetchone()
    if data:
        return {"img": data[0], "caption": data[1]}

def change_post(img, caption, menu_name):
    c.execute("UPDATE posts SET img=?, caption=? WHERE menu_name=?", (img, caption, menu_name))
    conn.commit()

def get_all_posts():
    data = c.execute("SELECT img, caption, menu_name FROM posts").fetchall()
    posts = []
    for i in data:
        posts.append({"img": i[0], "caption": i[1], "menu_name": i[2]})
    return posts


def close_database():
    conn.close()


def default():
    c.execute("CREATE TABLE IF NOT EXISTS users (id, name, status)")
    c.execute("CREATE TABLE IF NOT EXISTS referals (user_id, reffer_id, status)")
    c.execute("CREATE TABLE IF NOT EXISTS posts (img, caption, menu_name)")
    conn.commit()
    for i in ("Mening taklif havolam", "Sovg'alar"):
        if not get_post(menu_name=i):
            c.execute("INSERT INTO posts (img, caption, menu_name) VALUES (?, ?, ?)", (None, None, i))
            

default()

