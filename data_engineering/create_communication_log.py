import pymysql
import credentials
from faker import Faker
import random
import connect_to_database

fake = Faker()


# Create a cursor object
cursor = connect_to_database.connection.cursor()

# Execute a query to select a specific column from a table
column_name = 'customer_id'  # Replace 'column_name_here' with your column name
table_name = 'Customer'    # Replace 'table_name_here' with your table name
query = f"SELECT {column_name} FROM {table_name}"

cursor.execute(query)

# Fetch the results
customer_ids = cursor.fetchall()

# Print the selected column
print(customer_ids)

communication = ['Phone Call','Email','Online Chat','In-Person Visit','Letter','Mobile App']

# status = ['Active','Inactive/Dormant','Closed','Blocked/Frozen','Limited/Restricted','Defaulted']

def create_communications():
    communications_data = []

    for customer_id in customer_ids:

        # Generate a random number between 1 and 10 (you can adjust the range)
        # One person can have maximum of 5 accounts
        random_iterations = random.randint(1, 20)

        # Run the for loop for the random number of times
        for i in range(random_iterations):
            # Generate a fake account_id
            fake_log_id = fake.port_number()
            print("Fake_log_id:", fake_log_id)

            #Generate a fake account type
            communication_type = random.choice(communication)

            #Generate a fake status
            # status_type = random.choice(status)

            # Generate a fake balance
            fake_timestamp = fake.time()
            print("Fake timestamp:", fake_timestamp)

            #create a tuple named row
            row = (fake_log_id,customer_id[0],communication_type,fake_timestamp)
            # print(row)
            #append into customer_data_list
            communications_data.append(row)

            print(f"This is iteration number {i + 1}")

    return communications_data
    
# def delete_duplicates():
#     # Execute a query to select a specific column from a table
#     column_name = 'account_id'  # Replace 'column_name_here' with your column name
#     table_name = 'Account'    # Replace 'table_name_here' with your table name
#     query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
#     return query

#Run the create accounts function
accounts = create_communications()

# SQL statement to perform the insertions
insert_account = """
    INSERT INTO CommunicationLog (log_id, customer_id, communication_type, timestamp)
    VALUES (%s, %s, %s, %s)
"""

# Execute the SQL statement for each set of data
for entry in accounts:
    cursor.execute(insert_account, entry)
    print(entry)

# Commit the changes to the database
connect_to_database.connection.commit()

#Delete any duplicates
# cursor.execute(delete_duplicates())

# # Commit the changes to the database
# connect_to_database.connection.commit()
     
# Close the cursor and connection
cursor.close()
        