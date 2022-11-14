import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, password, db_name):
    connect = None
    try:
        connect = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            database=db_name
        )
        print("Connection Successful")
    except Error as err:
        print(f"Error: {err}")
    return connect


def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        print("Query Execute Successfully")
    except Error as err:
        print(f"Error : {err}")


def read_query(connect, query):
    cursor = connect.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as err:
        print(f"Error: {err}")
    return result


pw = "Smprajkta4$"

db = "job_seeker_data"

connection = create_server_connection("localhost", "root", pw, db)

q1 = '''
select * From Upload;
'''

results = read_query(connection, q1)

for result in results:
    print(result)

q2 = '''
select user_id, path From Upload where processed_state = 0;
'''

results = read_query(connection, q2)

if results is not None:
    for result in results:
        print(result)
        print(type(result[1]))
        user_id = result[0]
else:
    print("Results is None")


print(user_id)
connection = create_server_connection("localhost", "root", pw, db)
q3 = f'''
UPDATE upload
SET processed_state = 1
WHERE user_id = '{user_id}';
'''

execute_query(connection, q3)
