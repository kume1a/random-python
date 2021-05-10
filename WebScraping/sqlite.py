import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

# c.execute("CREATE TABLE friends (name TEXT, age REAL);")

def insertOne():
    query = "INSERT INTO friends VALUES (?,?)"
    data = ("sampleName", 17.4)

    c.execute(query, data)

def insertMany():
    people = [
        ("Roald", 23),
        ("Rosa", 10),
        ("Neil", 18)
    ]

    query = "INSERT INTO friends VALUES (?,?)"
    c.executemany(query, people)

def selecting():
    c.execute("SELECT * FROM friends WHERE age > 12 ORDER BY age;")
    # for column in c:
    #     print(column)

    # oneItem = c.fetchone()  # <-- c is an iterator so fetching oneitem is like calling next()
    allAsList = c.fetchall()

    print(allAsList)


selecting()
# insertMany()

conn.commit()
conn.close()

'''
CREATE TABLE dogs ( -- create table
    name TEXT,
    breed TEXT,
    age INTEGER
);

INSERT INTO dogs (name, breed, age) VALUES ("Maggie", "Bulldog", 2); -- insert into a table
INSERT INTO dogs (name, breed, age) VALUES ("River", "Husky", 4);    -- insert into a table
INSERT INTO dogs (name, breed, age) VALUES ("Archer", "Pitbull", 8); -- insert into a table
INSERT INTO dogs (name) VALUES ("onlyName");                         -- insert into a table
-- SELECT * FROM dogs; -- print all columns of table
-- SELECT name FROM dogs; -- print name columns of table
-- SELECT name, age FROM dogs; -- print name and age columns of table

-- SELECT * FROM dogs WHERE name="River"; -- print all columns of table where name="River"
-- SELECT * FROM dogs WHERE name IS NOT "River" AND breed IS NOT "Pitbull";

-- SELECT * FROM dogs WHERE age > 3 ORDER BY age;

-- SELECT * FROM dogs WHERE name LIKE "%gg%";
'''