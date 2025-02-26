# DBMS-Economy-Database-With-UI

Economics Database Project

Overview
This repository contains SQL files necessary for creating an economics-oriented database with various tables. Additionally, it includes Python scripts for inserting new values into the tables, SQL syntax for reading, updating, and deleting tuples, as well as different types of queries such as Nested, Join, Aggregate, Procedure, Trigger, and Privileges.

Contents

* Dump folder: Contains all SQL files required for creating the database with necessary tables.

* Create_d.py: Python file for inserting new values into the tables within the database.

* Read_d.sql: SQL syntax for reading data from all the tables in the database.

* Update_d.sql: SQL syntax for updating tuples within the tables of the database.

* Delete_d.sql: SQL syntax for deleting tuples from the tables in the database.

* Query_d.sql: Includes various complex SQL queries:

* Nested queries
* Join operations
* Aggregate functions
* Stored Procedures
* Triggers
* Privileges setup and management

*Usage
Creating the Database
Use the SQL files in the 'Dump' folder to create the database and its tables.
Example:mysql -u username -p database_name < dump_file.sql

* Once everything is setup run : streamlit run main.py

Performing CRUD Operations
Create_d.py for inserting new values into tables.
Read_d.py for reading data from tables.
Update_d.py for updating tuples within tables.
Delete_d.py for deleting tuples from tables.
For complex queries: Refer Query_d

Adding more SQL queries or scripts that enhance database functionalities.
Improving existing Python scripts for better performance or clarity.
Reporting issues or bugs that need attention.

# Acknowledgments
[IMF(International Monetary Fund) World Economy Data.]


  
