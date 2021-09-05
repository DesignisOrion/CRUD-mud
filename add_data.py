import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('1','DesignIsOrion', '12345')")
cursor.execute("INSERT INTO users VALUES ('2','GLDNFLabs', 'temp')")
cursor.execute("INSERT INTO users VALUES ('3','DataIsOrion', 'abcde')")
cursor.execute("INSERT INTO users VALUES ('4','OBIOS', 'beta')")
cursor.execute("INSERT INTO users VALUES ('5','SoundRound', 'sound')")
cursor.execute("INSERT INTO users VALUES ('6','Admin', 'Admin')")


connection.commit()
