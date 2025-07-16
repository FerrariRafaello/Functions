import sqlite3


class LambdaExamples:
    @staticmethod
    def simple_add():
        add = lambda x, y: x + y
        print(add(10, 20))
        print(add(15, 17))
        print(add("mascos", "castro"))

    @staticmethod
    def capture_variable():
        x = 10
        a = lambda y: x + y
        x = 20
        b = lambda y: x + y
        print(a(10))  # 30, because x=20 at call time
        print(b(10))  # 30

    @staticmethod
    def lock_variable_in_lambda():
        x = 10
        a = lambda y, x=x: x + y  # x locked as 10
        x = 20
        b = lambda y, x=x: x + y  # x locked as 20
        print(a(10))  # 20
        print(b(10))  # 30


class CharutosCubanosDB:
    def __init__(self, db_name="banco.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CharutosCubanos (
                symbol TEXT,
                shares INTEGER,
                price REAL
            )
            """
        )
        self.connection.commit()

    def insert_stocks(self, stocks):
        self.cursor.executemany(
            "INSERT INTO CharutosCubanos VALUES (?, ?, ?)", stocks
        )
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM CharutosCubanos")
        return self.cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    print("=== Lambda examples ===")
    LambdaExamples.simple_add()
    LambdaExamples.capture_variable()
    LambdaExamples.lock_variable_in_lambda()

    print("\n=== SQLite3 database demo ===")
    db = CharutosCubanosDB()
    db.connect()
    db.create_table()
    stocks = [
        ("garibald", 400, 1000),
        ("garibaldur", 300, 2000),
        ("garibalde", 100, 7500),
    ]
    db.insert_stocks(stocks)
    rows = db.fetch_all()
    for row in rows:
        print(row)
    db.close()
