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

credit_score = ['800 - 850','740 - 799','670 - 739','580 - 669','300 - 579']



def create_credit_history():
    credit_data = []

    for customer_id in customer_ids:
        # Generate a fake credit_id
        # Generate a random number between 1 and 10 (you can adjust the range)
        # One person can have maximum of 5 accounts
        random_iterations = random.randint(1, 5)

        # Run the for loop for the random number of times
        for i in range(random_iterations):
            fake_credit_id = fake.port_number()
            print("Fake credit_id:", fake_credit_id)

            #Generate a fake account type
            fake_fico_credit_score = random.choice(credit_score)

            # Generate a credit_limit
            fake_credit_limit = fake.random_number()
            print("Fake credit_limit:", fake_credit_limit)

            #create a tuple named row
            row = (fake_credit_id,customer_id[0],fake_fico_credit_score,fake_credit_limit)
            # print(row)
            #append into customer_data_list
            credit_data.append(row)

            print(f"This is iteration number {i + 1}")
            
    return credit_data
    
# def delete_duplicates():
#     # Execute a query to select a specific column from a table
#     column_name = 'account_id'  # Replace 'column_name_here' with your column name
#     table_name = 'Account'    # Replace 'table_name_here' with your table name
#     query = f"DELETE t1 FROM {table_name} t1 JOIN (SELECT {column_name} FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1) t2 ON t1.{column_name} = t2.{column_name};"
#     return query

#Run the create accounts function
credits = create_credit_history()

# SQL statement to perform the insertions
insert_account = """
    INSERT INTO CreditHistory (credit_id, customer_id, credit_score, credit_limit)
    VALUES (%s, %s, %s, %s)
"""

# Execute the SQL statement for each set of data
for entry in credits:
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
        