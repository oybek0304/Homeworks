-- Easy
-- 1. Define the following terms: data, database, relational database, and table.
Data - Information that is stored and processed by a computer, which can be in various forms such as text, numbers, images, etc.
Database - A structured collection of data that is stored and managed by a database management system (DBMS), allowing for efficient data retrieval and manipulation.
Relational Database - A type of database that organizes data into tables (relations) that can be linked—or related—based on data common to each. It uses a schema to define the structure of the data.  
Table - A collection of related data entries that consists of rows and columns, where each row represents a record and each column represents a field in the record.

-- 2. List five key features of SQL Server.
1. **Scalability** - SQL Server can handle large volumes of data and support a high number of concurrent users.
2. **Security** - It provides robust security features, including authentication, authorization, and encryption.
3. **High Availability** - SQL Server supports features like Always On Availability Groups, which ensure that databases are available even in case of hardware failures.
4. **Data Integrity** - It enforces data integrity through constraints, triggers, and transactions.
5. **Advanced Analytics** - SQL Server includes built-in support for advanced analytics, including machine learning and data mining capabilities.

-- 3. What are the different authentication modes available when connecting to SQL Server? (Give at least 2)
1. **Windows Authentication** - Uses Windows user accounts to authenticate users, leveraging the security features of the Windows operating system.
2. **SQL Server Authentication** - Uses SQL Server-specific user accounts and passwords for authentication, allowing users to connect to the database without relying on Windows accounts.  


-- Medium
-- 4. Create a new database in SSMS named SchoolDB.
Create Database SchoolDb;

-- 5. Write and execute a query to create a table called Students with columns: StudentID (INT, PRIMARY KEY), Name (VARCHAR(50)), Age (INT).
USE SchoolDb;
Create Table Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);

-- 6. Describe the differences between SQL Server, SSMS, and SQL.
SQL Server - A relational database management system (RDBMS) developed by Microsoft that provides a platform for storing, retrieving, and managing data in databases. It supports various data types, transactions, and security features.
SSMS (SQL Server Management Studio) - A graphical user interface (GUI) tool provided by Microsoft for managing SQL Server instances. It allows users to create, modify, and query databases, as well as manage server configurations and security settings.
SQL (Structured Query Language) - A standard programming language used to manage and manipulate relational databases. It is used to perform tasks such as querying data, updating records, and creating database structures. SQL is the language that is executed by SQL Server to perform operations on the data.

-- Hard

-- 7. Research and explain the different SQL commands: DQL, DML, DDL, DCL, TCL with examples.
DQL (Data Query Language) - Used to query and retrieve data from a database.
   Example: `SELECT * FROM Students;`

DML (Data Manipulation Language) - Used to manipulate data within a database.
   Example: `INSERT INTO Students (Name, Age) VALUES ('Oybek Yuldoshev', 21);`

DDL (Data Definition Language) - Used to define and manage database structures.
   Example: `CREATE TABLE Courses (CourseID INT PRIMARY KEY, Title VARCHAR(100));`

DCL (Data Control Language) - Used to control access to data within a database.
   Example: `GRANT SELECT ON Students TO User1;`

TCL (Transaction Control Language) - Used to manage transactions within a database.
   Example: `COMMIT;`

-- 8. Write a query to insert three records into the Students table.
INSERT INTO Students (StudentID , Name, Age) VALUES
(1, 'Oybek Yuldoshev',21),
(2, 'Lionel Messi',38),
(3, 'Cristiano Ronaldo',40);

-- 9. Restore AdventureWorksDW2022.bak file to your server. (write its steps to submit)
-- Steps to restore AdventureWorksDW2022.bak file to your server:
-- 1. Open SQL Server Management Studio (SSMS).
-- 2. Connect to your SQL Server instance.
-- 3. Right-click on the "Databases" node in the Object Explorer.
-- 4. Select "Restore Database..." from the context menu.
-- 5. In the "Restore Database" dialog, select "Device" and click on the "..." button to browse for the backup file.
-- 6. Add the backup file (AdventureWorksDW2022.bak) and click OK.
-- 7. Choose the restore options as needed and click OK to start the restore process.
