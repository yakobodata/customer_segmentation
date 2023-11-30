import pymysql
import credentials
from faker import Faker

fake = Faker()
# Connect to the database
connection = pymysql.connect(
    user = credentials.user,
    password = credentials.password,
    host = credentials.host,
    database = credentials.database,
)

# Create a cursor object
cursor = connection.cursor()

# Execute a query to select a specific column from a table
column_name = 'customer_id'  # Replace 'column_name_here' with your column name
table_name = 'Customer'    # Replace 'table_name_here' with your table name
query = f"SELECT {column_name} FROM {table_name}"

cursor.execute(query)

# Fetch the results
selected_column = cursor.fetchall()

# Print the selected column
print(selected_column)

account_type = ['Savings Account','Checking/Current Account','Certificate of Deposit (CD)','Individual Retirement Account (IRA)','Business Accounts','Trust Accounts','Custodial Accounts']

status = ['Active','Inactive/Dormant','Closed','Blocked/Frozen','Limited/Restricted','Defaulted']

def create_accounts():
    accounts_data = []
# Close the connection
connection.close()
