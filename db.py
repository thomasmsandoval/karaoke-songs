import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS songs;
        """
    )
    conn.execute(
        """
        CREATE TABLE songs (
          id INTEGER PRIMARY KEY NOT NULL,
          title TEXT,
          artist TEXT,
          album TEXT,
          genre TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    songs_seed_data = [
        ("Bohemian Rhapsody", "Queen", "A Night at the Opera", "Rock"),
        ("Shape of You", "Ed Sheeran", "Divide", "Pop"),
        ("Billie Jeam", "Michael Jackson", "Thriller", "POP/R&B"),
        ("Hotel California", "Eagles", "Hotel California", "Rock")

    ]
    conn.executemany(
        """
        INSERT INTO songs (title, artist, album, genre)
        VALUES (?,?,?)
        """,
        songs_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()
