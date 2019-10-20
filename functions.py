import psycopg2, time, datetime, os,  calendar, getpass
try:
    # required information to use the db 
    conn = psycopg2.connect(
        database = "Python_Project", # database name
        user = "postgres",
        password = "MacBookPro", #your password
        host = "127.0.0.1",
        port = "5432"
    )

#Registration:
    def newUser():
        cursor = conn.cursor()
        print(" ")
        print("""****** NEW USER REGISTRATION ******
        """)

        fName = input("Enter your first name >> ").title()
        lName = input("Enter your last name >> ").title()        
        phone = input("Enter your phone number >> ")        
        username = input("Enter your username >> ")
        while True:
                password1 = getpass.getpass(prompt="Enter your password: ")
                password2 = getpass.getpass(prompt="Enter your password again: ")
                if password1 == password2:
                    password = password1 = password2
                    break
                else:
                    print(" ")
                    print(" The passwords you entered do not match! Try again!")
                    print(" ")
                
        userAddress = input("Enter your home address >> ")        
        zipCode = input("Enter your zip code >> ")        
        answer1 = input("What is your middle name? >> ").lower()     
        answer2 = input("Where were you born? >> ").lower()

        cursor.execute("""INSERT INTO users (first_name, last_name, phone_number, username, user_pass, user_address, zip_code, answer1, answer2) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (fName, lName, phone, username, password, userAddress, zipCode, answer1, answer2)
        )
        print("Welcome, " + fName)
        time.sleep(3)
        conn.commit()
        cursor.close()

    
        
  

    
  
#Authentication
    def auth(): 
        print("""
        ****** PLEASE LOG IN ******
        """)        
        username = input("username: ")
        password = getpass.getpass(prompt="password: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND user_pass=%s", (username, password))
        rows = cursor.fetchall()
        file = open("log.txt", 'a' )
        now = datetime.datetime.now()
        if(rows):
            
            print("""You have succesfully logged in!""")
            time.sleep(3)
            file.write(f"User {username} logged in at {now}\n")
            x = 0
        else:
            print("""Wrong credentials""")
            time.sleep(3)
            file.write(f"Someone tried to log in using this username: '{username}' at {now}\n")
            x = 1
            file.close()
        cursor.close()


#Reservaciones 
    def reservation():
        global username
        cursor = conn.cursor()
#Validating MONTH
        x = 1
        while x == 1:
            
            global time
            print("")
            print("""       
            ****** RESERVATION ******
            
            """)
            print(""" 
            Pick a Month option:

            1. January
            2. February
            3. March
            4. April
            5. May
            6. June
            7. July
            8. August
            9. September
            10. October
            11. November
            12. December

            """)  
            
            while True:
                try:
                    print(" ")
                    choice = int(input("Select an option from [1-12] >> "))
                    if choice in list(range(1,13)):
                      break
                    else:
                        print(" ")
                        print("""Wrong entry!!!""")
                       

                except: 
                    print(" ")
                    print(""""Please, enter only integer numbers between [1-12].""")
                    
        
            if choice == 1:
                month = "January"  
                print(" ") 
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 2:
                month = "February"
                print(" ")  
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 3:
                month = "March"  
                print(" ")
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 4:
                month = "April"
                print(" ")
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 5:
                month = "May"
                print(" ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 6:
                month = "June"
                print(" ")   
                print(f"You selected {month}.") 
                print(" ") 
                x = 0
            if choice == 7:
                month = "July"
                print(" ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 8:
                month = "August"
                print("  ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 9:
                month = "September"
                print(" ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 10:
                month = "October"
                print(" ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 11:
                month = "November"
                print(" ")   
                print(f"You selected {month}.")
                print(" ") 
                x = 0
            if choice == 12:
                month = "December"
                print(" ")  
                print(f"You selected {month}.")
                print(" ") 
                x = 0
                         
# Validating DAY
            x = 1    
            while x == 1:
                global calendar
                
                if month == "January":
                    y = int(2019)
                    m = int(1)
                    print(calendar.month(y, m)) 
                elif month == "February":
                    y = int(2019)
                    m = int(2)
                    print(calendar.month(y, m)) 
                elif month == "March":
                    y = int(2019)
                    m = int(3)
                    print(calendar.month(y, m)) 
                elif month == "April":
                    y = int(2019)
                    m = int(4)
                    print(calendar.month(y, m)) 
                elif month == "May":
                    y = int(2019)
                    m = int(5)
                    print(calendar.month(y, m)) 
                elif month == "June":
                    y = int(2019)
                    m = int(6)
                    print(calendar.month(y, m)) 
                elif month == "July":
                    y = int(2019)
                    m = int(7)
                    print(calendar.month(y, m)) 
                elif month == "August":
                    y = int(2019)
                    m = int(8)
                    print(calendar.month(y, m))     
                elif month == "September":
                    y = int(2019)
                    m = int(9)
                    print(calendar.month(y, m))
                elif month == "October":
                    y = int(2019)
                    m = int(10)
                    print(calendar.month(y, m))     
                elif month == "November":
                    y = int(2019)
                    m = int(11)
                    print(calendar.month(y, m))
                elif month == "December":
                    y = int(2019)
                    m = int(12)
                    print(calendar.month(y, m))

#Selecting a reservation day
                while True:
                    try:
                        print("")
                        selectedDay = int(input("Select a day from the calender >> "))
                        if choice in list(range(1,31)):
                            break
                        else:
                            print(" ")
                            print("""Wrong entry!!!""")
                            
                    except:
                        print(" ")
                        print(""""Please, enter only integer numbers.""")
                         

                if month == "February":
                    if selectedDay not in list(range(1,29)):
                        print("")
                        print("""The month you selected only has 28 days. Try to enter a valid day number""")
                         
                        x = 1
                    elif selectedDay in list(range(1,29)):
                        day = selectedDay
                        print("")
                        print(f"""You selected day number {day}. """)
                         
                        x = 0

                elif month == "April" or month == "June" or month == "September" or month == "November":
                    if selectedDay not in list(range(1,31)):
                        print("")
                        print("""The month you selected only has 30 days. Try to enter a valid day number""")
                         
                        x = 1
                    elif selectedDay in list(range(1,31)):
                        day = selectedDay
                        print("")
                        print(f"""You selected day number {day}! """)
                         
                        x = 0

                elif month == "January" or "March" or "May" or "July" or "August" or "October" or "December":
                    if selectedDay not in list(range(1,32)):
                        print("")
                        print("""The month you selected only has 31 days. Try to enter a valid day number""")
                         
                        x = 1
                    elif selectedDay in list(range(1,32)):
                        day = selectedDay
                        print("")
                        print(f"""You selected day number {day}. """)
                         
                        x = 0
                    


 #Validating TIME
        x = 1
        while x == 1:
            print(" ")
            print(""" What time do you want yout appointment ? :

                    1. 8:00am
                    2. 9:00am
                    3. 10:00am
                    4. 11:00am
                    5. 1:00pm
                    6. 2:00pm
                    7. 3:00pm
                    8. 4:00pm
                    9. 5:00pm
                    """)  

            while True:
                    try:
                        print(" ")
                        selectedTime = int(input("Select a time for your appointment  >> "))
                        if choice in list(range(1,10)):
                            break
                        else:
                            if selectedTime not in list(range(1,10)):
                                print(" ")    
                                print("""Wrong option! Select an option in the menu.""")
                            

                    except:
                        print("")
                        print(""""Please, enter only integer numbers.""")
                         


            if selectedTime == 1:
                time = "8:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0

            if selectedTime == 2:
                time = "9:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                 
                x = 0

            if selectedTime == 3:
                time = "10:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0

            if selectedTime == 4:
                time = "11:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0

            if selectedTime == 5:
                time = "1:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
              
                x = 0

            if selectedTime == 6:
                time = "2:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0    

            if selectedTime == 7:
                time = "3:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0

            if selectedTime == 8:
                time = "4:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
                
                x = 0

            if selectedTime == 9:
                time = "5:00"
                print(" ")
                print(f"""You selected your appointment to be at {time}. """)
               
                x = 0

                

#Validating SERVICES
        x = 1
        while x == 1:
            print("""        ****   SERVICES   ****

                        1. MANICURE............$18

                        2. PEDICURE............$18 
                                
            """)

            selectedService = input("Select a service >> ")

            if selectedService != "1" and selectedService != "2":
                print(" ")
                print("""Wrong option! Select an option in the menu [1-2].""")
               
                x = 1
                
            elif selectedService == "1":
                service = "Manicure"
                print(" ")
                print(f"""You selected {service} service.""" )
                
                x = 0

            elif selectedService == "2":
                service = "Pedicure"
                print(" ")
                print(f"""You selected {service} service""" )
                
                x = 0
          

#Validating TECHNICIAN
        x = 1
        while x == 1:
            
            print("""       *** Technicians *** 

                    1. Maria

                    2. Carla

                    3. Yulimar """
            )
            selectedTech = input("Select a technician: >> ")
            if selectedTech != "1" and selectedTech != "2" and selectedTech != "3":
                print(" ")
                print("""Wrong option! Select an option in the menu [1-3].""")
                
                x = 1

            elif selectedTech == '1':
                print(" ")
                technician = "Maria"
                print(f"""You selected {technician} as your Technician""")
                
                x = 0

            elif selectedTech == '2':
                print(" ")
                technician = "Carla"
                print(f"""You selected {technician} as your Technician""")
                
                x = 0

            elif selectedTech == '3':
                print(" ")
                technician = "Yulimar"
                print(f"""You selected {technician} as your Technician""")
                
                x = 0
        
#Checking if row exits and inserting info into reservations table
        cursor.execute("SELECT * FROM Reservations WHERE reservation_month=%s AND reservation_day=%s AND reservation_time=%s AND reservation_technician=%s", (month, day, time, technician))
        rows = cursor.fetchall()
        if(rows):
            print(" ")
            print("""Someone already scheduled an appointment with these attributes. Try a different time, day or technitian""")
            x = 1
        else:
            cursor.execute("""INSERT INTO reservations (reservation_month, reservation_day, reservation_time, reservation_service, reservation_technician)
            VALUES (%s, %s, %s, %s, %s)""", (month, day, time, service, technician)
        ) 
            x = 0
        cursor.close()


#inserting info in order table
      
        username = 'dearsea'
        cursor.execute
        (
        """SELECT FROM Users WHERE username=%s""", (username)
        )

        cursor.execute
        (
        """SELECT FROM Reservations WHERE username = %s""", (username)
        )

        cursor.execute
        (
        """SELECT FROM Services WHERE service_nam = %s""", (service)
        )

        cursor.execute
        (
        """INSERT INTO orders(user_id, reservation_id, service_id, service_nam, service_price) 
        VALUES (%s, %s, %s, %s, %s)""", (user_id, reservation_id, service, service_price)
        ) 
        x = 0
        cursor.close()





    #     def retrieveAllUserInfo(user, passW):
    #         cursor = conn.cursor()
    #     cursor.execute(*f"SELECT  FROM auth WHERE username='{user}' AND pass='{passW}'")
    #     rows=cursor.fetchall()
    #     if(rows):
    #         for row in rows:
    #             role=row[2]
    #         if(role=="administrator"):
    #             print(f"{user}, you have been authenticated. You're an admnistrator")
    #         else:
    #             print(f"{user}, you have been authenticated. You're a user")
    #     else:
    #         print("User does not exist")    
    #     cursor.close()   
    # usernameInput = input("Enter your username >> ")
    # passwordInput = input("Enter your password >> ")
    # retrieveAllUserInfo(usernameInput, passwordInput)


 
    
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from your database", error)

