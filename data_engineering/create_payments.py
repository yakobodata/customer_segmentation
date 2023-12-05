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

payment_method = ['Credit Card','Debit Card','Cash','Mobile Payment','Bank Transfer','E-wallet','Cryptocurrency','Contactless Card','Check','Prepaid Card']

def create_payments():
    payments_data = []

    for account_id in account_ids:

        # Generate a random number between 1 and 10 (you can adjust the range)
        # One person can have maximum of 5 accounts
        random_iterations = random.randint(1, 50)

        # Run the for loop for the random number of times
        for i in range(random_iterations):
            # Generate a fake account_id
            fake_payment_id = fake.port_number()
            print("Fake payment_id:", fake_payment_id)

            # Generate a fake amount
            fake_receipient = fake.company()
            print("Fake receipient:", fake_receipient)


            # Generate a fake amount
            fake_amount = fake.random_number()
            print("Fake amount:", fake_amount)

            # Generate a fake payment_date
            fake_payment_date = fake.date()
            print("Fake payment date:", fake_payment_date)

            #Generate a fake payment method
            fake_payment_method = random.choice(payment_method)

            #create a tuple named row
            row = (fake_payment_id,account_id[0],fake_receipient,fake_amount,fake_payment_date,fake_payment_method)
            # print(row)
            #append into customer_data_list
            payments_data.append(row)

            print(f"This is iteration number {i + 1}")

    return payments_data
    
# def delete_duplicates():
#     # Execute a query to select a specific column from a table
#     column_name = 'account_id'  # Replace 'column_name_here' with your column name
#     table_name = 'Account'    # Replace 'table_name_here' with your table name
#     query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
#     return query

#Run the create accounts function
payments = create_payments()

# SQL statement to perform the insertions
insert_payment = """
    INSERT INTO Payment (payment_id, account_id, recipient, amount, payment_date, payment_method)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

# Execute the SQL statement for each set of data
for entry in payments:
    cursor.execute(insert_payment, entry)
    print(entry)

# Commit the changes to the database
connect_to_database.connection.commit()

#Delete any duplicates
# cursor.execute(delete_duplicates())

# # Commit the changes to the database
# connect_to_database.connection.commit()
     
# Close the cursor and connection
cursor.close()
        