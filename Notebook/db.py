import sqlite3

with sqlite3.connect("note_book.db") as db:
    # Create Cursor
    cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS notes(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    note_name TEXT,
    note_body TEXT,
    record_time TEXT
   )
""")
db.commit()


def saving_note(note):
    cur.execute("INSERT INTO users(note_name, note_body, record_time) VALUES(?, ?, ?)", note)
    db.commit()

def looking_data(note_name):
    cur.execute("SELECT * FROM users WHERE lname = ?", (note_name,))
    records = cur.fetchall()
    for row in records:
        print('ID:', row[0])
        print('Заголовок:', row[1])
        print('Тело заметки', row[3], end='\n\n')

def looking_all():
    cur.execute("SELECT * FROM notes")
    records = cur.fetchall()
    for row in records:
        print(row[2], row[1])

def delete_data(note_name):
    cur.execute("DELETE FROM notes WHERE (note_name, note_body) = (?)", (note_name,))
    db.commit()
    print(f"Контакт '{note_name}' удален")
            
def changing_note(note_name):
    cur.execute("UPTADE notes SET ")
