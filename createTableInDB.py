import sqlite3

# this should be run only once in a while, for testing purposes.
# once the DB is created in a fully working fashion this should not be used.

# connect to db and create table
def add_information_to_db(db):
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE files (
                    file_name text NOT NULL,
                    file_scale text NOT NULL,
                    file_codec text NOT NULL,
                    file_output_name text NOT NULL,
                    media BLOB NOT NULL
    )""")

    conn.commit()
    conn.close()


add_information_to_db('image-database.db')