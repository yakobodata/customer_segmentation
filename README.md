#  Customer_segmentation
Problem - Marketing teams in financial services are unable to properly target marketing content to desired clients.
Solution - Customer segmentation using data 
Target consumers - Marketing Team

#  Objectives and Scope
## Objective
Identify and segment customers based on behavior, demographics, or financial activity.

## Scope
Determine the specific attributes and criteria for segmentation (e.g., transaction history, demographics, interaction frequency).

# Data Collection and Integration
# Data Sources
Customer databases, transactional data, CRM systems, demographic data sources

## Create a customer database schema 

![Customer Database Schema](customer_segmentation\data_engineering\images\customer_database_schema_version_1.png)

## Create different tables 
```
create database customers;

show databases;

use customers;

CREATE TABLE Customer (
    customer_id INT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(255),
    date_of_birth DATE,
    identification_number VARCHAR(50)
);


CREATE TABLE Account (
    account_id INT ,
    customer_id INT,
    account_type VARCHAR(50),
    balance DECIMAL(18, 2),
    status VARCHAR(20),
);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(50),
    amount DECIMAL(18, 2),
    transaction_date DATETIME,
    notes TEXT,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    account_id INT,
    recipient VARCHAR(100),
    amount DECIMAL(18, 2),
    payment_date DATE,
    payment_method VARCHAR(50),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE CreditHistory (
    credit_id INT PRIMARY KEY,
    customer_id INT,
    credit_score INT,
    credit_limit DECIMAL(18, 2),
    payment_history TEXT,
    credit_utilization DECIMAL(5, 2),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Security (
    security_id INT PRIMARY KEY,
    customer_id INT,
    username VARCHAR(50),
    password VARCHAR(100),
    access_level VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Relationships (
    relationship_id INT PRIMARY KEY,
    customer1_id INT,
    customer2_id INT,
    relationship_type VARCHAR(50),
    FOREIGN KEY (customer1_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (customer2_id) REFERENCES Customer(customer_id)
);

CREATE TABLE CommunicationLog (
    log_id INT PRIMARY KEY,
    customer_id INT,
    communication_type VARCHAR(50),
    timestamp DATETIME,
    summary TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Compliance (
    compliance_id INT PRIMARY KEY,
    customer_id INT,
    consent_given BOOLEAN,
    disclosures TEXT,
    regulatory_requirements_met BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
```
## Have data populated into that database tables
Inorder to populate the tables in the database am going to have to connect to the database and then populated the different table using a python library called faker

- Connect to database
```
import mysql.connector
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

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
```


## Have a functional database running



# Tools
-   Amazon Web Services(AWS)
-   MySQL Workbench

# Python Libraries
-   Faker
-   mysql-connector-python
-   pymysql
-   random


03/12/2023
Am now working on the accounts table

Working on credit history table