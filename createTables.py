import psycopg2
try:
    # required information to use the db 
    conn = psycopg2.connect(
        database = "Python_Project", # database name
        user = "postgres",
        password = "MacBookPro", #your password
        host = "127.0.0.1",
        port = "5432"
    )
    def createTables(): # function to create the tables
        cursor = conn.cursor()
        # create table users: To save user authentication information
        cursor.execute(
            """CREATE TABLE Users (
			User_id SERIAL NOT NULL PRIMARY KEY,
			First_name text NOT NULL,
            Last_name text NOT NULL,
			Phone_number text NOT NULL,
            Username text NOT NULL,
            User_pass text NOT NULL,
            User_address text NOT NULL,
            Zip_code text NOT NULL,
            Answer1 text NOT NULL,
            Answer2 text NOT NULL)"""
		)
        conn.commit()
        #create table reservations
        cursor.execute(
            """CREATE TABLE Reservations (
			Customer_id serial NOT NULL PRIMARY KEY,
            First_name text NOT NULL,
            Last_name text NOT NULL,
			Phone_number text NOT NULL,
            Month_sch text NOT NULL,
            Day_sch text NOT NULL,
            Time_sch text NOT NULL,
            Service_sch text NOT NULL, 
            Package_sch text NOT NULL,
            Technician text NOT NULL)"""
		)
        conn.commit()
        #create table services
        cursor.execute(
            """CREATE TABLE Services (
			Service_id serial NOT NULL PRIMARY KEY,
            Service_nam text NOT NULL,
			Service_price real NOT NULL,
            Technician text NOT NULL)"""
        )
        conn.commit()
        #create table packages
        cursor.execute(
            """CREATE TABLE Packages ( 
            Package_id serial NOT NULL PRIMARY KEY,
            Package_nam text NOT NULL,
            Package_price real NOT NULL,
            Technician text NOT NULL)"""
        )
        conn.commit()
        #create table payments where we save the payment information of the usersss
        cursor.execute(
            """CREATE TABLE Payments (
			User_id serial NOT NULL PRIMARY KEY,
            First_name text NOT NULL,
            Last_name text NOT NULL,
            Phone_number text NOT NULL,
			Card_number text NOT NULL,
            Card_name text NOT NULL
            Sec_number text NOT NULL)
            Zip_code text NOT NULL)"""
        )
        conn.commit()
        cursor.close()  
    createTables()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)