# import connect_to_database
from faker import Faker

fake = Faker()

def make_customers():
    
    # # Data to be inserted
    # data = [
    #     (1, 'John Doe', 'john@example.com', '123-456-7890', '123 Main St, City, Country', '1990-05-15', 'ID12345'),
    #     (2, 'Jane Smith', 'jane@example.com', '987-654-3210', '456 Oak St, Town, Country', '1985-10-25', 'ID67890'),
    #     (3, 'Alice Johnson', 'alice@example.com', '555-123-4567', '789 Elm St, Village, Country', '1995-02-08', 'ID54321')
    # ]
    
    customer_data = []
    # Repeat the code a million times
    for _ in range(500):
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
        row = (fake_customer_id,fake_name,fake_phone,fake_email,fake_address,fake_date_of_birth,fake_identification_number,fake_gender)
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
