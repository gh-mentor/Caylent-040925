import sqlite3

class LoginManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def login(self, username, password):
        self.connect_to_db()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(query)

        result = self.cursor.fetchone()

        if result:
            return True  # Login successful
        else:
            return False  # Login failed