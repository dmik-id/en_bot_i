import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
# cur.execute('''CREATE TABLE users (id VARCHAR(255), lang VARCHAR(255))''')


cur.execute('''CREATE TABLE users_requests (id VARCHAR(255), lang VARCHAR(255), input VARCHAR(255), translate VARCHAR(255))''')