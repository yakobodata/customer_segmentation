import mysql.connector
# import create_customers
import credentials
# Replace these variables with your actual database credentials

def connect():
    db_config = {
        'user': credentials.user,
        'password': credentials.password,
        'host': credentials.host,
        'database': credentials.database,
    }


    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            return connection
            # return connection
            # Perform operations here (e.g., execute queries)
            #populate the database
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")



