import sqlite3

conn = sqlite3.connect('inventory.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


# Ensure that the inventory table exists
cursor.executescript('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY autoincrement,
    barcode TEXT unique,
    location TEXT,
    name TEXT NOT NULL,
    UNIQUE (id, name)
);

CREATE TABLE if not exists checkout_log (
    id INTEGER PRIMARY KEY autoincrement, 
    checkoutTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    userId INTEGER NON NULL,
    itemID INTEGER NON NULL, 
    returned BOOL DEFAULT FALSE
);

CREATE TABLE if not exists users (
    userId INTEGER primary key autoincrement,
    actualName text unique,
    password text unique 
);

CREATE TABLE if not exists user_log (
    id INTEGER primary key autoincrement,
    theTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    attemptedPassword text,
    userId integer,
    action text,
    authenticated BOOL
);
''')
cursor.connection.commit()

del cursor

def _get_cursor():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()

def add_user(name, password):
    conn, c = _get_cursor()
    c.execute("INSERT INTO users (actualName, password) VALUES (?, ?)", (name, password))
    conn.commit()


def check_login(password):
    _, c = _get_cursor()
    row = c.execute("SELECT userId from users where password = ? LIMIT 1;", [password]).fetchone()
    if row is None:
        return None

    return row["userId"]


def add_item(name, location=None, barcode=None):
    conn, c = _get_cursor()
    c.execute("INSERT into inventory (location, name, barcode) VALUES (?, ?, ?)", (location, name, barcode))
    conn.commit()


def set_location(id, location):
    conn, c = _get_cursor()
    c.execute("UPDATE inventory SET location = ? WHERE id = ?", (location, id))
    conn.commit()


def use_item(id, user_id):
    conn, c = _get_cursor()
    c.execute("INSERT into checkout_log (itemID, userId, returned) VALUES (?, ?, false)", (id, user_id))
    conn.commit()


def return_item(id, user_id):
    conn, c = _get_cursor()
    c.execute("INSERT into checkout_log (itemID, userId, returned) VALUES (?, ?, true)", (id, user_id))
    conn.commit()


def set_location_barcode(barcode, location):
    conn, c = _get_cursor()
    c.execute("UPDATE inventory SET location = ? WHERE barcode = ?", (location, barcode))
    cursor = conn.cursor()


def use_item_barcode(barcode, user_id):
    conn, c = _get_cursor()
    c.execute(
            "INSERT into checkout_log (itemID, userId, returned) VALUES ((SELECT inventory.id from inventory where barcode = ?), ?, false)",
            (barcode, user_id))
    conn.commit()


def return_item_barcode(barcode, user_id):
    conn, c = _get_cursor()
    c.execute(
            "INSERT into checkout_log (itemID, userId, returned) VALUES ((SELECT inventory.id from inventory where barcode = ?), ?, true)",
            (barcode, user_id))
    conn.commit()


def set_barcode(itemId, barcode):
    conn, c = _get_cursor()
    c.execute("UPDATE inventory set barcode = ? where id = ?", (barcode, itemId))
    conn.commit()


def get_all_items():
    conn, c = _get_cursor()
    rows = c.execute(
            "with itemsReturned as (\n    select max(id) as max_id, itemID, not(returned) as in_use\n    from checkout_log\n    group by itemID)\n\n\nselect inventory.id, barcode, location, name, IFNULL(in_use, FALSE) as in_use\nfrom inventory left outer join itemsReturned on inventory.id = itemID;").fetchall()
    return [dict(i) for i in rows]


def log_event(user_id=None, attempted_password=None, action=None, authenticated=False):
    conn, c = _get_cursor()
    c.execute("INSERT INTO user_log (userId, attemptedPassword, action, authenticated) VALUES (?, ?, ?, ?)", (user_id, attempted_password, action, authenticated))
    conn.commit()
