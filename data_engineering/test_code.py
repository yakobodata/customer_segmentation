from faker import Faker

fake = Faker()

customer_data = []
# Repeat the code a million times
for _ in range(1000000):
    # Generate a fake customer_id
    fake_customer_id = fake.random_number()
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