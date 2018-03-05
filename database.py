import sqlite3
import os


class Database:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        Database.create_table_customers()
        Database.create_table_tickets()
        Database.customer()

    def file_check(self):
        if os.path.exists('database.db'):
            pass

    def delete_database(self):
        if os.path.exists('database.db'):
            os.remove('database.db')

    def create_table_customers(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE Customers (Id INT, Name TEXT)")

    def create_table_tickets(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE Tickets (Ticket INT, Time INT, OrderBy STR, Status STR, Type STR, Total INT, Location STR, Elapsed INT")

    def customer(self):
        cur = self.con.cursor()
        cur.execute("INSERT INTO Customers VALUES(1, 'Michelle')")
        cur.execute("INSERT INTO Customers VALUES(2, 'Howard')")
        cur.execute("INSERT INTO Customers VALUES(3, 'Greg')")

    def ticket(self):
        cur = self.con.cursor()
        cur.execute("INSERT INTO Tickets VALUES(1, '0:30', 'Loni', 'Closed', 'Delivery', '19.99', '461 W Delilah Rd', '0:30'")