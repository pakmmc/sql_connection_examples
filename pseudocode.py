import SOMETHING

# 1. OPEN THE DATABASE:
connection = SOMETHING.connect()
cursor = connection.cursor()

# (Note: Python requires you to always
#  create a cursor when connecting to a database.
#  Cursors are supposed to be a useful way
#  to paginate the results of a large query,
#  but in Python they're a bit of a misapplied abstraction
#  that end up getting used for all queries,
#  even when we typically fetch all the results at once.
#  It's not something we really need to worry about in great detail.)

# 2. RUN YOUR SQL:
sql = "SELECT * FROM users"
cursor.execute(sql)

# 3. CHOOSE WHICH OF THESE ACTIONS YOU WOULD LIKE TO PERFORM:
# result = cursor.fetchone() # Get a single row
# result = cursor.fetchall() # Get a list of rows
# connection.commit() # Save any changes you made to the database

# 4. CLOSE THE DATABASE:
cursor.close()
connection.close()
