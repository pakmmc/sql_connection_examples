# Running pymysql requires installing MySQL
# (The whole suite, not just MySQL Workbench:
# https://dev.mysql.com/downloads/installer/ )
# and installing the python pymysql library
# ( py -m pip install pymysql ).

# It has more connection settings than sqlite3,
# but that makes it more secure,
# and pymysql has the added advantage that it
# has been set up to close itself properly
# when we use the Python 'with _ as _' syntax.
import pymysql

# Put pymysql.connect(...) into a function
# so we don't have to repeat it every time we connect
def create_connection():
    return pymysql.connect(
        # host="10.0.0.17",      # Address of the school server
        # user="mmc",            # Your school username
        host="localhost",    # Addess of your personal home server
        user="root",         # Your home MySQL username
        password="********",   # Your password, a 5-letter word starting with A
        db="mmc_test",         # The name of your database
        charset="utf8mb4",     # Fix MySQL's text encoding: 'UTF8-Max-Bytes-4'
        cursorclass=pymysql.cursors.DictCursor
                               # Make the cursor return Python dictionaries
                               # ( {'key1': 'value1', 'key2': 'value2'} )
                               # instead of tuples ( ('value1', 'value2') )
    )

# 'with _ as _ ' is a special Python syntax
#  that will automatically run '.close()'
#  at the end of the block, even if an error occurs.
# (FYI, This also works for nicely opening and closing files.)

with create_connection() as connection:
    with connection.cursor() as cursor:

        # DON'T allow arbitrary changes to SQL.
        # Instead, pass a tuple of values to cursor.execute
        # so that users can't sabotage your SQL.
        sql = "SELECT * FROM users WHERE id = %s"
        values = (1, )
        cursor.execute(sql, values)

        # result = cursor.fetchone()
        result = cursor.fetchall()
        # connection.commit()

        print(result)
