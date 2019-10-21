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
###### MISSING VALIDATIONS FOR DATA TYPE AND UNIQUE CONSTRAINT*******
        # cursor.execute(
        #     """CREATE TABLE Users (
		# 	user_id SERIAL NOT NULL PRIMARY KEY,
		# 	first_name text NOT NULL,
        #     last_name text NOT NULL,
		# 	phone_number text NOT NULL,
        #     username text UNIQUE,
        #     user_pass text NOT NULL,
        #     user_address text NOT NULL,
        #     zip_code text NOT NULL,
        #     answer1 text NOT NULL,
        #     answer2 text NOT NULL)"""
		# )
        # conn.commit()
        # #create table reservations
        # cursor.execute(
        #     """CREATE TABLE Reservations (
		# 	reservation_id serial NOT NULL PRIMARY KEY,     
        #     reservation_month text NOT NULL,
        #     reservation_day smallint NOT NULL,
        #     reservation_time text NOT NULL,
        #     reservation_service text NOT NULL, 
        #     reservation_technician text NOT NULL,
        #     username text,
        #     FOREIGN KEY (username) REFERENCES Users(username)
        #     ) """
		# )
        # conn.commit()


        # #create table services
        # cursor.execute(
        #     """CREATE TABLE Services (
		# 	service_id serial NOT NULL PRIMARY KEY,
        #     servicename CHARACTER(20) UNIQUE,
		# 	service_price money UNIQUE 
        #     ) """
        # )
        # conn.commit()


        # #create table payments where we save the payment information of the users
        # cursor.execute(
        #     """CREATE TABLE Payments (
        #     payment_id serial NOT NULL PRIMARY KEY,    
		# 	card_number text NOT NULL,
        #     card_name text NOT NULL,
        #     security_number text NOT NULL,
           
        #     user_id INT,
        #     FOREIGN KEY (user_id) REFERENCES Users(user_id))"""
        # )
        # conn.commit()



        #create table orders where every order is stored
        cursor.execute(
            """CREATE TABLE Orders (
			order_id serial NOT NULL PRIMARY KEY,
           
            username TEXT,
            FOREIGN KEY (username) REFERENCES Users(username),

            servicename TEXT,
            FOREIGN KEY (servicename) REFERENCES Services(servicename),

            service_price  money,
            FOREIGN KEY (service_price) REFERENCES Services(service_price),

            processed_order boolean NOT NULL )"""
        )
        conn.commit()


        cursor.close()  
    createTables()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)