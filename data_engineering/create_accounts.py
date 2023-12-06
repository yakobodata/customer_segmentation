import pymysql
import credentials
from faker import Faker
import random
from connect_to_database import connect
fake = Faker()
import csv
# Create a cursor object
connection = connect()

cursor = connection.cursor()
print(connection)


# Execute a query to select a specific column from a table
column_name = 'customer_id'  # Replace 'column_name_here' with your column name
table_name = 'Customer'    # Replace 'table_name_here' with your table name
query = f"SELECT {column_name} FROM {table_name}"

cursor.execute(query)

# Fetch the results
customer_ids = cursor.fetchall()

# Print the selected column
print(customer_ids)

account = ['Savings Account','Checking/Current Account','Certificate of Deposit (CD)','Individual Retirement Account (IRA)','Business Account','Trust Account','Custodial Account']

status = ['Active','Inactive/Dormant','Closed','Blocked/Frozen','Limited/Restricted','Defaulted']

def create_accounts():
    accounts_data = []

    for customer_id in customer_ids:

        # Generate a random number between 1 and 10 (you can adjust the range)
        # One person can have maximum of 5 accounts
        random_iterations = random.randint(1, 5)

        # Run the for loop for the random number of times
        for i in range(random_iterations):
            # Generate a fake account_id
            fake_account_id = fake.port_number()
            print("Fake customer_id:", fake_account_id)

            #Generate a fake account type
            account_type = random.choice(account)

            #Generate a fake status
            status_type = random.choice(status)

            # Generate a fake balance
            fake_balance = fake.random_number()
            print("Fake balance:", fake_balance)

            #create a tuple named row
            row = (fake_account_id,customer_id[0],account_type,fake_balance,status_type)
            # print(row)
            #append into customer_data_list
            accounts_data.append(row)

            print(f"This is iteration number {i + 1}")

    # Convert tuples to a list of tuples
    data_list = [list(row) for row in accounts_data]

    # File name to save
    file_name = 'accounts_data_tuples.csv'

    # Writing data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)

    print(f'Data from tuples has been written to {file_name}')
    return accounts_data
    
# def delete_duplicates():
#     # Execute a query to select a specific column from a table
#     column_name = 'account_id'  # Replace 'column_name_here' with your column name
#     table_name = 'Account'    # Replace 'table_name_here' with your table name
#     query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
#     return query

# #Run the create accounts function
# accounts = create_accounts()

# # SQL statement to perform the insertions
# insert_account = """
#     INSERT INTO Account (account_id, customer_id, account_type, balance, status_type)
#     VALUES (%s, %s, %s, %s, %s)
# """

# # Execute the SQL statement for each set of data
# for entry in accounts:
#     cursor.execute(insert_account, entry)
#     print(entry)

# Commit the changes to the database
# connection.commit()

# #Delete any duplicates
# # cursor.execute(delete_duplicates())

# # # Commit the changes to the database
# # connect_to_database.connection.commit()
     
# # Close the cursor and connection
# cursor.close()
# Query to load data from file into MySQL table
load_data_query = """
    LOAD DATA INFILE 'accounts_data_tuples.csv'
    INTO TABLE Account
    FIELDS TERMINATED BY 'account_id, customer_id, account_type, balance, status_type'
    LINES TERMINATED BY '\\n'
    IGNORE 1 LINES;
"""


# Execute the LOAD DATA INFILE query
cursor.execute(load_data_query)
# Commit the changes
connection.commit()
print("Data loaded successfully")
cursor.close()
connection.close()