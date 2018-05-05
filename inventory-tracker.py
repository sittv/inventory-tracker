# SITTV Inventory Tracker
# Copyright 2018 SITTV
# Mostly an adapted rewrite of Jesse Stevenson's shirt tracker

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# File should be in format [ID Location Name] with spaces separating


import sqlite3


conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()


# Ensure that the inventory table exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER NOT NULL PRIMARY KEY,
    location TEXT NOT NULL DEFAULT "free",
    name TEXT NOT NULL,
    UNIQUE (id, name)
)
''')
cursor.connection.commit()


def list_all_items():
    """
    Display all items in the database.
    """
    cursor.execute('''
    SELECT * FROM inventory ORDER BY id
    ''')
    for id, location, name in cursor:
        print(id, location, name)


def list_item():
    """
    Display an item matching the criterion.
    """
    method = input('List by id, name, or location? ').lower()
    if method not in {'id', 'name', 'location'}:
        print('Please specify a list method.')
        return

    search = input('Enter ' + method + ': ')

    cursor.execute('SELECT * FROM inventory WHERE ' + method + ' = ?', (search,))
    items = cursor.fetchall()
    if items is None:
        print('Item not found')
        return

    for id, location, name in items:
        print(id, location, name)


def delete_item():
    """
    Find any items matching a search and delete them.
    """
    method = input('Delete id or name? ').lower()
    if method not in {'id', 'name'}:
        print('Please choose a valid lookup method.')
        return

    if method == 'id':
        id = input('ID: ')
        cursor.execute('DELETE FROM inventory WHERE id = ?', (id,))
    elif method == 'name':
        name = input('Name: ')
        cursor.execute('DELETE FROM inventory WHERE name = ?', (name,))

    cursor.connection.commit()


def use_item():
    """
    Set the location of an item to 'inuse'
    """
    method = input('Select item by id or name?  ').lower()
    if method not in {'id', 'name'}:
        print('Please choose a valid lookup method.')
        return

    if method == 'id':
        id = input('ID: ')
        cursor.execute('UPDATE inventory SET location = "inuse" WHERE id = ?', (id,))
    elif method == 'name':
        name = input('Name: ')
        cursor.execute('UPDATE inventory SET location = "inuse" WHERE name = ?', (name,))

    cursor.connection.commit()


def add_item():
    """
    Get the fields from the user and add an item to the database.

    If a matching item is already in the database, it will not add the item to
    the database.
    """
    id = input('ID: ')
    location = input('Location: ')
    name = input('Name: ')

    cursor.execute('''
    SELECT * FROM inventory WHERE id = ?
    ''', (id,))

    if cursor.fetchone():
        print('Item with that ID already exists')
        return

    cursor.execute('''
    SELECT * FROM inventory WHERE name = ?
    ''', (name,))

    if cursor.fetchone():
        print('Item with that name already exists')
        return

    cursor.execute('''
    INSERT INTO inventory VALUES (?, ?, ?)
    ''', (id, location, name))

    cursor.connection.commit()


def set_location(new_location):
    method = input('Change location by name or ID? ').lower()
    if method not in {'id', 'name'}:
        print('Please select a valid lookup method.')
        return

    search = input('Enter ' + method + ': ')
    
    cursor.execute('''
    UPDATE inventory
    SET location = ?
    WHERE %s = ?
    ''' % method, (new_location, search))

    cursor.connection.commit()


def retag():
    raise SystemExit


try:
    while True:
        function = input('\n'.join(['\n\nAvailable commands:', 'list', 'listall', 'add',
                                    'delete', 'use', 'set', 'bye, exit, (q)uit']) + '\n\n')
        if function == 'list':
            list_item()
        elif function == 'listall':
            list_all_items()
        elif function == 'add':
            add_item()
        elif function == 'delete':
            delete_item()
        elif function == 'use':
            use_item()
        elif function == 'set':
            set_location(input('Enter a new location: '))
        elif function in {'bye', 'exit', 'q', 'quit'}:
            exit()
        elif function == 'red-button':
            class SelfDestruct(Exception):
                """
                Every good inator needs a way to self destruct
                """

            wiki_page = '''
Self-destructive behavior is any behavior that is harmful or
potentially harmful towards the person who engages in the behavior.

Self-destructive behaviors exist on a continuum, with suicide at one
extreme end of the scale.[1] Self-destructive actions may be
deliberate, born of impulse, or developed as a habit. The term however
tends to be applied toward self-destruction that either is fatal, or
is potentially habit-forming or addictive and thus potentially
fatal. Self-destructive behavior is often associated with mental
illnesses such as borderline personality disorder[2] or
schizophrenia.[3][4]

Acts of "self-destruction" may be merely metaphorical ("social
suicide") or literal (suicide).

Types of self-destructive behavior
* Suicide
* Self-harm
* Eating disorders [medical citation needed]
* Substance abuse

Self-destructive behavior may be used as a coping mechanism when one
is overwhelmed. For example, faced with a pressing scholastic
assessment, someone may choose to sabotage their work rather than cope
with the stress. This would make submission of (or passing) the
assessment impossible, but remove the worry associated with it.

Self-destructive behavior may also manifest itself in an active
attempt to drive away other people. For example, they may fear that
they will "mess up" a relationship. Rather than deal with this fear,
socially self-destructive individuals engage in annoying or alienating
behavior, so that others will reject them first.

More obvious forms of self-destruction are eating disorders, alcohol
abuse, drug addictions, sex addiction, self-injury, and suicide
attempts.

An important aspect of self-destructive behavior is the inability to
handle the stress stemming from an individual's lack of
self-confidence – for example in a relationship, whether the other
person is truly faithful ("how can they love someone like me?"); at
work or school, whether the realization of assignments and deadlines
is possible ("there is no way I can complete all my work on
time"). Self-destructive people usually lack healthier coping
mechanisms, like asserting personal boundaries. As a result, they tend
to feel that showing they are incompetent is the only way to untangle
themselves from demands.

Successful individuals may self-destructively sabotage their own
achievements; this may stem from a feeling of anxiety, unworthiness,
or from an impulsive desire to repeat the "climb to the top."

Self-destructive behavior is often considered to be synonymous with
self-harm, but this is not accurate. Self-harm is an extreme form of
self-destructive behavior, but it may appear in many other guises.'''

            raise SelfDestruct(wiki_page)
        else:
            print('Please enter a valid command.')

except (EOFError, KeyboardInterrupt):
    exit()
