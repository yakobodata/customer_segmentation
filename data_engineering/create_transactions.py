import pymysql
import credentials
from faker import Faker
import random
import connect_to_database

fake = Faker()


# Create a cursor object
cursor = connect_to_database.connection.cursor()

# Execute a query to select a specific column from a table
column_name = 'account_id'  # Replace 'column_name_here' with your column name
table_name = 'Account'    # Replace 'table_name_here' with your table name
query = f"SELECT {column_name} FROM {table_name}"

cursor.execute(query)

# Fetch the results
account_ids = cursor.fetchall()

# Print the selected column
print(account_ids)

transaction_type = ['Purchase','Financial','Online','Credit','Investment','Payment ','Subscription','Wire']


def create_transactions():
    transactional_data = []

    for account_id in account_ids:

        # Generate a random number between 1 and 10 (you can adjust the range)
        # One person can have maximum of 5 accounts
        random_iterations = random.randint(1, 100)

        # Run the for loop for the random number of times
        for i in range(random_iterations):
            # Generate a fake transaction_id
            fake_transaction_id = fake.port_number()
            print("Fake transaction_id:", fake_transaction_id)

            # Generate a fake transaction type
            fake_transaction_type = random.choice(transaction_type)
            print("Fake transaction_type:", fake_transaction_type)


            # Generate a fake amount
            fake_amount = fake.random_number()
            print("Fake amount:", fake_amount)

            # Generate a fake transactional_date
            fake_transactional_date = fake.date()
            print("Fake transactional date:", fake_transactional_date)

            #Generate a fake payment method
            # fake_payment_method = random.choice(payment_method)

            #create a tuple named row
            row = (fake_transaction_id,account_id[0],fake_transaction_type,fake_amount,fake_transactional_date)
            # print(row)
            #append into customer_data_list
            transactional_data.append(row)

            print(f"This is iteration number {i + 1}")

    return transactional_data
    
def delete_duplicates():
    # Execute a query to select a specific column from a table
    column_name = 'account_id'  # Replace 'column_name_here' with your column name
    table_name = 'Account'    # Replace 'table_name_here' with your table name
    query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
    return query

#Run the create accounts function
transactions = create_transactions()

# SQL statement to perform the insertions
insert_transaction = """
    INSERT INTO Transaction (transaction_id, account_id, transaction_type, amount, transaction_date)
    VALUES (%s, %s, %s, %s, %s)
"""

# Execute the SQL statement for each set of data
for entry in transactions:
    cursor.execute(insert_transaction, entry)
    print(entry)

# Commit the changes to the database
connect_to_database.connection.commit()

# Delete any duplicates
cursor.execute(delete_duplicates())

# Commit the changes to the database
connect_to_database.connection.commit()
     
# Close the cursor and connection
cursor.close()
        