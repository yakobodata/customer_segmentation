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

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")

        # Perform operations here (e.g., execute queries)
        #populate the database
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # SQL statement to perform the insertions
        insert_customers = """
            INSERT INTO Customer (customer_id, name, email, phone, address, date_of_birth, identification_number,gender)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        customers = create_customers.make_customers()

        # Execute the SQL statement for each set of data
        for entry in customers:
            cursor.execute(insert_customers, entry)
            print(entry)

        # Commit the changes to the database
        connection.commit()

        #Delete any duplicates
        cursor.execute(create_customers.delete_duplicates())

        # Commit the changes to the database
        connection.commit()
        # Close the cursor and connection
        cursor.close()
        

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
