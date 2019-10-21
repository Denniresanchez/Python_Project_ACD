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
            """INSERT INTO Users (first_name, last_name, phone_number, username, user_pass, user_address, zip_Code, answer1, answer2)
            VALUES ('Dennire', 'Sanchez', '7866303833', 'dearsea', 'mnbv0987', 'Sunny Isles blvd', '33160', 'valencia', 'cecilia')""" 
		) 
        conn.commit()
    insertUsers()



    # function to insert reservations 
    def insertReservations(): 
        cursor = conn.cursor()
    # insert reservations into database
        cursor.execute(
                """INSERT INTO Reservations (reservation_month, reservation_day, reservation_time, reservation_service,  reservation_technician, username)
                VALUES ('10', '10', '10:00AM',  'Manicure','Maria', 'dearsea')"""
            ) 
        conn.commit()
    insertReservations()




    #___________________________________________________________________________
    # function to insert services
    def insertServices(): 
        cursor = conn.cursor()
    # insert services into database
        cursor.execute(
                """INSERT INTO Services (servicename, service_price)
                VALUES ('Manicure', 18), 
                ('Pedicure', 16),
                ('Mani&Pedi', 32),
                ('Regular Facial', 80),
                ('Special Facial', 150),
                ('Eyebrows Waxing', 12)"""
            ) 
        conn.commit()
    insertServices()
    #___________________________________________________________________________






# function paymentmethod into database
    def insertPaymentInfo(): 
        cursor = conn.cursor()
# insert paymentmethod into database
        cursor.execute(
                """INSERT INTO Payments (card_number, card_name, security_number, user_id)
                VALUES ('5476354687659876', 'Dennire Sanchez', '854', 1)"""
            ) 
        conn.commit()
    insertPaymentInfo()


#  # function to insert orders
    def insertOrders(): 
        cursor = conn.cursor()
# insert orders into database
        cursor.execute(
                """INSERT INTO Orders (user_id, reservation_id, service_id, service_price)
                VALUES (1, 1, 1, 18)
                """
            ) 
        conn.commit()
    insertOrders()
       
  

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)