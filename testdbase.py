import sqlite3
class Testdbase(object):
    def __init__(self, name="database.db"):
        self.name = name
        self.con = sqlite3.connect(self.name)
        self.cur = self.con.cursor()
        self.createTables()

    def createTables(self):
        
        # Namen
        sql = '''
        CREATE TABLE IF NOT EXISTS name 
        (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    VARCHAR(200),
            vorname VARCHAR(200)
        );
        '''
        self.cur.execute(sql)

    # Name
    def save_name(self, name, vorname):
        sql='''
        INSERT INTO name (name, vorname) VALUES (?,?);
        '''
        self.cur.execute(sql, (name, vorname))
        self.con.commit()