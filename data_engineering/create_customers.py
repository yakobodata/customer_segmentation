# import connect_to_database
from faker import Faker
from connect_to_database import connect
import subprocess
# import mysql.connector
fake = Faker()
# Run another Python script
# subprocess.run(["python", "connect_to_database.py"])
# Create a cursor object to interact with the database

# Execute the INSERT query for each set of values
connection = connect()

cursor = connection.cursor()
print(connection)

def make_customers():
    customer_data = []
    # Repeat the code a million times
    for _ in range(10000):
        # Generate a fake customer_id
        fake_customer_id = fake.port_number()
        print("Fake customer_id:", fake_customer_id)

        # Generate a fake name
        fake_name = fake.name()
        print("Fake name:", fake_name)

        # Generate a fake name
        fake_phone = fake.basic_phone_number()
        print("Fake phone:", fake_phone)

        # Generate a fake email address
        fake_email = fake.email()
        print("Fake Email:", fake_email)

        # Generate a fake address
        fake_address = fake.address()
        print("Fake Address:", fake_address)

        # Generate a fake date_of_birth
        fake_date_of_birth = fake.date_of_birth()
        print("Fake date_of_birth:", fake_date_of_birth)

        # Generate a fake identification_number
        fake_identification_number = fake.passport_number()
        print("Fake identification_number:", fake_identification_number)

        # Generate a fake gender
        fake_gender = fake.passport_gender()
        print("Fake gender:", fake_gender)

        #create a tuple named row
        row = (fake_customer_id,fake_name,fake_email,fake_phone,fake_address,fake_date_of_birth,fake_identification_number,fake_gender)
        print(row)
        #append into customer_data_list
        customer_data.append(row)

    return customer_data

def delete_duplicates():
    # Execute a query to select a specific column from a table
    column_name = 'customer_id'  # Replace 'column_name_here' with your column name
    table_name = 'Customer'    # Replace 'table_name_here' with your table name
    query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
    return query


customers = make_customers()

# SQL statement to perform the insertions
insert_customers = """
    INSERT INTO Customer (customer_id, name, email, phone, address, date_of_birth, identification_number,gender)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute the SQL statement for each set of data
for entry in customers:
    cursor.execute(insert_customers, entry)
    print(entry)

# Commit the changes to the database
connection.commit()

#Delete any duplicates
cursor.execute(delete_duplicates())

# Commit the changes to the database
connection.commit()
# Close the cursor and connection
cursor.close()
        


