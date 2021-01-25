import sqlite3

from .score import Score

class DatabaseManager:
    """ This class is to manage a collection of scores on a database
    
    Attributes:
        _db : connection to database
        _cursor: allows us to execute SQL commands
    """
    def __init__(self, filename='scores.db'):
        """ Initialize our DatabaseManager class. If table doesn't exist create one
        Arg:
            filename (.db or .sqlite): database
        """
        self._db = sqlite3.connect(filename)
        self._cursor = self._db.cursor()

        self._cursor.execute('SELECT name from sqlite_master where type="table"')
        res = self._cursor.fetchone()
        if not res or "scores" not in res:
            self._cursor.execute(
                "CREATE TABLE scores (name TEXT NOT NULL, score INTEGER NOT NULL)"
            )
            self._db.commit()

    def get_all(self):
        """ This method is to all the scores from .db files. Return: nested list of the score"""
        self._cursor.execute("SELECT * FROM scores ORDER BY score DESC")
        return [
            Score(data[0], data[1])
            for data in self._cursor.fetchall()
        ]
        
    def add(self, name, score):
        """ This method is to add the score (with name of player) to .db file"""
        _ = Score(name, score)
        self._cursor.execute(f"INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
        self._db.commit()

    def remove_by_name(self, name):
        """ This method is to remove the score and the name of player in .db file with name arg"""
        self._cursor.execute("DELETE FROM scores WHERE name=?", (name, ))
        self._db.commit()
    
    def close(self):
        """ This method is close .db file after retrieve it"""
        self._db.close()


if __name__ == "__main__":
    manager = DatabaseManager("scores.db")
    data = manager.get_all()
    print(data)

    # manager.add("Test", 999)
    manager.remove_by_name("Joo")

#* python -m models.score_database_manager