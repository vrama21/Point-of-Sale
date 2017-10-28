import sqlite3
import os


class Database:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        Database.create_table()
        Database.customer()

    def file_check(self):
        if os.path.exists('database.db'):
            pass

    def delete_database(self):
        if os.path.exists('database.db'):
            os.remove('database.db')

    def create_table(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE Customers (Id INT, Name TEXT)")

    def customer(self):
        cur = self.con.cursor()
        cur.execute("INSERT INTO Customers VALUES(1, 'Michelle')")
        cur.execute("INSERT INTO Customers VALUES(2, 'Howard')")
        cur.execute("INSERT INTO Customers VALUES(3, 'Greg')")
