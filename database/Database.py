import sqlite3

class Database:

    def __init__(self, dbFile):
        try:
            self.conn = sqlite3.connect(dbfile, isolation_level=None, check_same_thread = False)
            self.conn.execute("CREATE TABLE IF NOT EXISTS Webpage (hash TEXT PRIMARY KEY, url TEXT, content TEXT);")
        except Exception as e:
            self.conn = ""

    def isConn(self):
        if self.conn:
            return True
        else:
            return False

    def saveData(self, hash, url, content):
        if self.conn:
            sql = "INSERT INTO Webpage (hash, url, content) VALUES (?, ?, ?);"
            self.conn.execute(sql, (hash, url, content) )
        else:
            raise sqlite3.OperationalError('Database is not connected. Can not save Data!')

    def close(self):
        if self.conn:
            self.conn.close()
        else:
            raise sqlite3.OperationalError('Database is not connected.')
