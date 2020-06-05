
                                # INSERT Command


import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO population VALUES('New York', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Fran', 'CA', 800000)")

conn.commit()
conn.close()


# Let's look at the above code re-written using the with keyword:
# with sqlite3.connect("new.db") as connection:
#     cursor = connection.execute()
#     cursor.execute("INSERT INTO population VALUES('New York', \
#     'NY', 840000)")
#     cursor.execute("INSERT INTO population VALUES('San Fran', \
#     'CA', 800000)")



