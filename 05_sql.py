# Let's refactor the code using Try/Except:

import sqlite3

conn = sqlite3.connect("new.db")
c = conn.cursor()

try:
    # insert data
    c.execute("INSERT INTO populations VALUES('New York', 'NY', 8400000)")
    c.execute("INSERT INTO populations VALUES('San Fran', 'CA', 800000)")

    # commit the changes
    conn.commit()

except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

# close the database connection
conn.close()


# import sqlite3            # This print it as tuple!!!
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     # use a for loop to iterate through the database, printing the results line by line
#     for row in c.execute("SELECT firstname, lastname from employees"):
#         print(row)



# Let's look at how to remove the unicode characters so we can output just the values:

# THIS PRINTS IT normal string no quotation

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname from employees")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()
    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])

    # in Flask notes check 3- Inserting data.py file
