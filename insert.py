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
    # function to insert users
    def insertUsers(): 
        cursor = conn.cursor()
    # insert users into database
        cursor.execute(
            """INSERT INTO Users (First_name, Last_name, Phone_number, Username, User_pass, User_address, Zip_Code, Answer1, Answer2)
            VALUES ('Dennire', 'Sanchez', '7866303833', 'dearsea', 'mnbv0987', 'Sunny Isles blvd', '33160', 'valencia', 'cecilia')""" 
		) 
        conn.commit()
    insertUsers()
    # function to insert reservations 
    def insertReservations(): 
        cursor = conn.cursor()
    # insert reservations into database
        cursor.execute(
                """INSERT INTO Reservations (First_name, Last_name, Phone_number, Month_sch, Day_sch, Time_sch, Service_sch, Package_sch, Technician)
                VALUES ('Dennire', 'Sanchez', '7866303833', '10', '10', '10',  'manicure',' ', '1')"""
            ) 
        conn.commit()
    insertReservations()
    # function to insert services
    def insertServices(): 
        cursor = conn.cursor()
    # insert services into database
        cursor.execute(
                """INSERT INTO Services (Service_nam, Service_price, Technician)
                VALUES ('Manicure', 18, '1'),
                ('Manicure', 18, '2'),
                ('Manicure', 18, '3')"""
            ) 
        conn.commit()
    insertServices()
     # function to insert packagesss
    def insertPackages():
        cursor = conn.cursor()
    # insert packages into database
        cursor.execute(
                """INSERT INTO Packages (Package_nam, Package_price, Technician)
                VALUES ('ManiAndPedi', 28, '1'),
                ('ManiAndPedi', 28, '2'),
                ('ManiAndPedi', 28, '3')"""
            )
        conn.commit()
    insertPackages()
# function to insert packages
    def insertPaymentInfo(): 
        cursor = conn.cursor()
# insert paymentmethod into database
        cursor.execute(
                """INSERT INTO Payments (First_name, Last_name, Phone_number, Card_number, Card_name, Sec_number, Zip_code)
                VALUES ('Dennire', 'Sanchez', '7866303833', '5476354687659876', 'Dennire Sanchez', '854', '33160')"""
            ) 
        conn.commit()
        cursor.close()
    insertPaymentInfo()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)