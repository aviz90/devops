import pymysql

# Establishing a connection to DB
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Password1!', db='users')
conn = pymysql.connect(host='remotemysql.com', port=3306, user='naHHXoNehK', passwd='zd0vDie8ni', db='naHHXoNehK')

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into naHHXoNehK.dogs (name, age, breed) VALUES ('dog_a', 2, 'pit')")
cursor.execute("INSERT into naHHXoNehK.dogs (name, age, breed) VALUES ('dog_b', 1, 'pincher')")
cursor.execute("INSERT into naHHXoNehK.dogs (name, age, breed) VALUES ('dog_c', 4, 'amstaf')")


# Deleting data into table
# cursor.execute("DELETE FROM users.players WHERE id = '7'")

# Updating data inside the table
cursor.execute("UPDATE naHHXoNehK.dogs SET name = 'dog_d' WHERE name = 'dog_a'")

# Getting all data from table “users”
cursor.execute("SELECT * FROM naHHXoNehK.dogs;")

# Iterating table and printing all users
for row in cursor:
    print(row)

conn.commit()
cursor.close()
conn.close()
