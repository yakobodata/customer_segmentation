import mysql.connector
import create_customers
import credentials
# Replace these variables with your actual database credentials
db_config = {
    'user': credentials.user,
    'password': credentials.password,
    'host': credentials.host,
    'database': credentials.database,
}

# Establish a connection to the database
connection = mysql.connector.connect(**db_config)

connection.close()
print("MySQL connection is closed")