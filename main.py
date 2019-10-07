import psycopg2, datetime, time
try:
    # required information to use the db 
    conn = psycopg2.connect(
        database = "Python_Project", # database name
        user = "postgres",
        password = "MacBookPro", #your password
        host = "127.0.0.1",
        port = "5432"
    )
    
    def verifyUser():
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE Phone_number='{pn}'")
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                # phone=row[4]
                # if(phone=='{phoneNumber}'):
                print("Hi, Welcome Back!")
                print("You are already registered!")
                # else:
                # print("You are not registered!")
        else:
           print("User does not exist!") 
        # conn.commit()
        cursor.close()
    pn= input("Please, enter your phone number ex. (305)-(000-0000)")
    verifyUser(pn)
    # #Log in 
    #         def authentication(): 
    #             cursor = conn.cursor()
    #             username = input("Enter your Username: ")
    #             password = input("Enter your Password: ")
    #             cursor.execute(
    #                 f"""SELECT * FROM Users WHERE Username='{username}' and User_pass='{password}'"""
    #             )
    #             conn.commit()
    #             rows = cursor.fetchall()
    #             cursor.close()
    #             file = open("log.txt", 'a' )
    #             now = datetime.datetime.now()
    #             if rows:
    #                 print("You have succesfully Logged in!")
    #                 file.write(f"User {username} logged in at {now}\n")
    #             else:
    #                 print("Wrong credentials")
    #                 file.write(f"Someone tried to login using this username '{username}' at {now}\n")
    #             file.close()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)