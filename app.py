import eel
import sqlite3

DB_PATH = "./out/data.db"

def make_table(db: sqlite3.Connection):
    cursor = db.cursor()
    SQL = """
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        tag1 text NOT NULL,
        tag2 text NOT NULL,
        tag3 text NOT NULL,
        description TEXT NOT NULL );
    """
    try:
        cursor.execute(SQL)
    except  sqlite3.Error as e:
        print(e)

@eel.expose
def write_to_file(s: str):
    print(s)
    with open('out/data.txt', 'w') as f:
        f.write(s)

@eel.expose
def print_data(s):
    print(s)

@eel.expose
def write_idea_to_db(idea: dict[str: str]):
    print(idea)
    cursor = db.cursor()
    SQL = "INSERT INTO ideas (name, tag1, tag2, tag3, description) VALUES (?, ?, ?, ?, ?);"
    try:
        cursor.execute(SQL, (idea['idea-name'], idea['tag-1'], idea['tag-2'], idea['tag-3'], idea['description']))
        db.commit()
    except sqlite3.Error as e:
        print(e)
    cursor.close()

@eel.expose
def get_all_ideas():
    cursor = db.cursor()
    ideas = cursor.execute("SELECT * FROM ideas")
    ideas = ideas.fetchall()
    cursor.close()
    return ideas

@eel.expose
def delete_entry(id):
    cursor = db.cursor()
    SQL = """DELETE FROM ideas WHERE id = (?);"""
    cursor.execute(SQL, (id,))
    db.commit()
    cursor.close()
    
if __name__ == "__main__":
    # database initialisation
    db = sqlite3.connect(DB_PATH)
    make_table(db)

    eel.init('static')
    #eel.start('index.html', mode='chrome', cmdline_args=['--auto-open-devtools-for-tabs'], size=(1000, 500))
    eel.start('index.html', mode='chrome', size=(1000, 500))