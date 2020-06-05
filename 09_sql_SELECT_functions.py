import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # create a dictionary of sql queries
    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population",
    }

    # run each sql query item in the dictionary
    for keys, values in sql.items():
        c.execute(values)
        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(keys + ":", round(result[0]))
