import psycopg2, time, datetime, os,  calendar, getpass, re

try:
#Required information to use the db 
    conn = psycopg2.connect(
        database = "Python_Project", # database name
        user = "postgres",
        password = "6108", #your password
        host = "127.0.0.1",
        port = "5432"
    )
    
    username = ""
#Registration Function:
    def newUser():
        cursor = conn.cursor()
        os.system('clear')
        global username 
        print(" ")
        print("""****** NEW USER REGISTRATION ******
        """)

        fName = input("Enter your first name >> ").title()
        lName = input("Enter your last name >> ").title() 
        phoneValid = False
        while(phoneValid == False):
            phone = input("Enter your phone number >> ")
            if(re.search("[a-zA-Z@_!#$%^&*()<>?/\|}{~:]", phone) or len(phone) != 10):
                print("")
                print("""Invalid phone format. Please enter a valid 10-digit phone number.
                """)
            else:
                phoneValid = True       
 


        #Check if username already exists in database
        usernameExists = True
        while usernameExists == True:
            username = input("Enter your username >> ")
            cursor.execute(f'SELECT username FROM Users WHERE username=%s', (username,))
            rows = cursor.fetchall()
            if(rows):
                print("Username already exists")
            else:
                usernameExists = False


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

        #zip code validation
        zipCodeValid = False
        while(zipCodeValid == False):
            zipCode = input("Enter your zip code >> ")
            if(re.search("[a-zA-Z@_!#$%^&*()<>?/\|}{~:]", zipCode) or len(zipCode) != 5):
                print("")
                print("""Invalid zip code format. Please enter a valid 5-digit zip code.
                """)
            else:
                zipCodeValid = True

        print("")
        print("Security Questions: ")      
        answer1 = input("What is your middle name? >> ").lower()     
        answer2 = input("Where were you born? >> ").lower()

        cursor.execute("""INSERT INTO users (first_name, last_name, phone_number, username, user_pass, user_address, zip_code, answer1, answer2) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (fName, lName, phone, username, password, userAddress, zipCode, answer1, answer2)
        )
        print(" ")
        print("Welcome, " + fName)
        time.sleep(3)
        conn.commit()
        cursor.close()
        x = 0
        

    

#Authentication Function
    def auth():
        global username
        while True:
            authChoice = input("""
            What would you like to do?
            1. Login
            2. Forgot Password
            >> """)
            if(authChoice == "1"):
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
                    print(" ")
                    print("""You have succesfully logged in!""")
                    time.sleep(3)
                    file.write(f"User {username} logged in at {now}\n")
                    return True
                #Add !if(rows): print("user does not exist")
                else:
                    print(" ")
                    print("""Wrong credentials""")
                    time.sleep(3)
                    file.write(f"Someone tried to log in using this username: '{username}' at {now}\n")
                    return False
                    file.close()
                cursor.close()
                break
            elif authChoice == "2":
                usernameExists = False
                cursor = conn.cursor()
                while usernameExists == False:
                    confirmUser = input("Enter your username to reset your password >> ")
                    cursor.execute(f'SELECT username FROM Users WHERE username=%s', (confirmUser,))
                    rows = cursor.fetchall()
                    if(rows):
                        while True:
                            print("")
                            print("Please answer the following security questions to confirm your identity...")
                            print("")
                            time.sleep(2)
                            securityAnswer1 = input("What is your middle name? >> ")
                            securityAnswer2 = input("Where were you born? >> ")

                            cursor.execute(f'SELECT answer1, answer2 FROM Users WHERE username=%s AND answer1=%s AND answer2=%s', (confirmUser, securityAnswer1, securityAnswer2,))
                            securityRows = cursor.fetchall()
                            if(securityRows):
                                print("Identity Confirmed. Please reset password")

                                while True:
                                    password1 = getpass.getpass(prompt="Enter your password: ")
                                    password2 = getpass.getpass(prompt="Enter your password again: ")
                                    if password1 == password2:
                                        cursor.execute(f'UPDATE Users SET user_pass=%s WHERE username=%s', (password1, confirmUser,));
                                        print("")
                                        print(f'Password for user {confirmUser} has been successfully updated. You may login with your new password')
                                        time.sleep(2)
                                        conn.commit()
                                        cursor.close()
                                        auth()
                                        break
                                    else:
                                        print(" ")
                                        print(" The passwords you entered do not match! Try again!")
                                        print(" ")
                                break
                            else:
                                print("Incorrect answer(s). Please try again.")

                        usernameExists = True
                        cursor.close()
                    else:
                        print("Username does not exist. Please try again.")
                break
            else:
                print("")
                print("Incorrect option. Please enter 1 or 2")



#Reservacion Funtion
    def reservation():
        global username
        cursor = conn.cursor()
        #Validation while loop
        x = 1
        while x == 1:
            
            global time
            os.system('clear')
            print(" ")
            print("""       
            ****** RESERVATION ******
            
            """)
            print(""" 
            Pick a month:

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
            #Validating range and data type. Handling exceptions.
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
                    
            #Conditionals to assign valiable selectedMonth
            if choice == 1:
                selectedMonth = "January"  
                print(" ") 
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 2:
                selectedMonth = "February"
                print(" ")  
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 3:
                selectedMonth = "March"  
                print(" ")
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 4:
                selectedMonth = "April"
                print(" ")
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 5:
                selectedMonth = "May"
                print(" ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 6:
                selectedMonth = "June"
                print(" ")   
                print(f"You've selected {selectedMonth}.") 
                print(" ") 
                x = 0
            if choice == 7:
                selectedMonth = "July"
                print(" ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 8:
                selectedMonth = "August"
                print("  ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 9:
                selectedMonth = "September"
                print(" ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 10:
                selectedMonth = "October"
                print(" ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 11:
                selectedMonth = "November"
                print(" ")   
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
            if choice == 12:
                selectedMonth = "December"
                print(" ")  
                print(f"You've selected {selectedMonth}.")
                print(" ") 
                x = 0
                         
# Validation while loop
            x = 1    
            while x == 1:
                global calendar
                #conditionals to display monthly calendar
                if selectedMonth == "January":
                    y = int(2019)
                    m = int(1)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "February":
                    y = int(2019)
                    m = int(2)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "March":
                    y = int(2019)
                    m = int(3)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "April":
                    y = int(2019)
                    m = int(4)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "May":
                    y = int(2019)
                    m = int(5)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "June":
                    y = int(2019)
                    m = int(6)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "July":
                    y = int(2019)
                    m = int(7)
                    print(calendar.month(y, m)) 
                elif selectedMonth == "August":
                    y = int(2019)
                    m = int(8)
                    print(calendar.month(y, m))     
                elif selectedMonth == "September":
                    y = int(2019)
                    m = int(9)
                    print(calendar.month(y, m))
                elif selectedMonth == "October":
                    y = int(2019)
                    m = int(10)
                    print(calendar.month(y, m))     
                elif selectedMonth == "November":
                    y = int(2019)
                    m = int(11)
                    print(calendar.month(y, m))
                elif selectedMonth == "December":
                    y = int(2019)
                    m = int(12)
                    print(calendar.month(y, m))

#Validating range and data type. Handling exceptions.
                while True:
                    try:
                        print(" ")
                        choice = int(input("Select a day from the calender >> "))
                        if choice in list(range(1,32)):
                            break
                        else:
                            print(" ")
                            print("""Wrong entry!!!""")
                            
                    except:
                        print(" ")
                        print(""""Please, enter only integer numbers.""")
                         
                #conditional to validate and assign selectedDay
                if selectedMonth == "February":
                    if choice not in list(range(1,29)):
                        print(" ")
                        print("""The month you've selected has only 28 days. Try to enter a valid day number""")
                        x = 1
                    elif choice in list(range(1,29)):
                        selectedDay = choice
                        print(" ")
                        print(f"""You selected day number {selectedDay}. """)
                        x = 0


                elif selectedMonth == "April" or selectedMonth == "June" or selectedMonth == "September" or selectedMonth == "November":
                    if choice not in list(range(1,31)):
                        print(" ")
                        print("""The month you selected has only 30 days. Try to enter a valid day number""")
                        x = 1
                    elif choice in list(range(1,31)):
                        selectedDay = choice
                        print(" ")
                        print(f"""You selected day number {selectedDay}. """)
                        x = 0

                elif selectedMonth == "January" or "March" or "May" or "July" or "August" or "October" or "December":
                    if choice not in list(range(1,32)):
                        print(" ")
                        print("""The month you selected has only 31 days. Try to enter a valid day number""")
                        x = 1
                    elif choice in list(range(1,32)):
                        selectedDay = choice
                        print(" ")
                        print(f"""You selected day number {selectedDay}. """)
                        x = 0


                        # selectedDay = choice
                        # print(" ")
                        # print(f"""You selected day number {selectedDay}. """)
                        # x = 0
                    


 #Validation while loop for selectedTime
        x = 1
        while x == 1:
            print(" ")
            print(""" What time do you want your appointment ? :

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
            ##Validating range and data type. Handling exceptions.
            while True:
                    try:
                        print(" ")
                        choice = int(input("Select a time for your appointment  >> "))
                        if choice in list(range(1,10)):
                            break
                        else:
                            if choice not in list(range(1,10)):
                                print(" ")    
                                print("""Wrong option! Select an option in the menu.""")

                    except:
                        print(" ")
                        print(""""Please, enter only integer numbers.""")
                         

            #conditionals to assign selectedTime
            if choice == 1:
                selectedTime = "8:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 2:
                selectedTime = "9:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 3:
                selectedTime = "10:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 4:
                selectedTime = "11:00AM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 5:
                selectedTime = "1:00PM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 6:
                selectedTime = "2:00PM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0    

            if choice == 7:
                selectedTime = "3:00PM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 8:
                selectedTime = "4:00PM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

            if choice == 9:
                selectedTime = "5:00PM"
                print(" ")
                print(f"""You selected your appointment to be at {selectedTime}. """)
                x = 0

                

#Validation while loop to select a service
        x = 1
        while x == 1:
            
            #services dictionary
            servicesoffer = {
            "Manicure" : 18, 
            "Pedicure" : 16, 
            "Mani and Pedi" : 32, 
            "Regular Facial" : 80, 
            "Special Facial" : 150, 
            "Eyebrows Waxing" : 12}

            print("""        
            ****   SERVICES   ****""")
            #for loop to print dictionary
            counter = 0
            for x, y in servicesoffer.items():
                print(f"{counter+1}. {x} ${y}")
                counter+= 1  
           
            print(" ")
            choice = input("Select a service >> ")

            if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
                print(" ")
                print("""Wrong option! Select an option in the menu [1-6].""")
                time.sleep(2)
                x = 1
                
            elif choice == "1":
                selectedService = "Manicure"
                service_price = 18
                print(" ")
                print(f"""You've selected {selectedService} service.""" )
                x = 0

            elif choice == "2":
                selectedService = "Pedicure"
                service_price = 16
                print(" ")
                print(f"""You've selected {selectedService} service""" )
                x = 0

            elif choice == "3":
                selectedService = "Mani and Pedi"
                service_price = 32
                print(" ")
                print(f"""You've selected {selectedService} service""" )
                x = 0

            elif choice == "4":
                selectedService = "Regular Facial"
                service_price = 80
                print(" ")
                print(f"""You've selected {selectedService} service""" )
                x = 0

            elif choice == "5":
                selectedService = "Special Facial"
                service_price = 150
                print(" ")
                print(f"""You've selected {selectedService} service""" )
                x = 0

            elif choice == "6":
                selectedService = "Eyebrows Waxing"
                service_price = 12
                print(" ")
                print(f"""You've selected {selectedService} service""" )
                x = 0
          

#Validating TECHNICIAN
        x = 1
        while x == 1:
            print(" ")
            print("""       
            *** Technicians *** 

            1. Maria

            2. Carla

            3. Yulimar """)
            
            choice = input("Select a technician: >> ")
            if choice != "1" and choice != "2" and choice != "3":
                print(" ")
                print("""Wrong option! Select an option in the menu [1-3].""")
                time.sleep(2)
                x = 1

            elif choice == '1':
                print(" ")
                technician = "Maria"
                print(f"""You've selected {technician} as your Technician""")
                x = 0

            elif choice == '2':
                print(" ")
                technician = "Carla"
                print(f"""You've selected {technician} as your Technician""")
                x = 0

            elif choice == '3':
                print(" ")
                technician = "Yulimar"
                print(f"""You've selected {technician} as your Technician""")
                x = 0
        
# Checking if row exits and inserting info into reservations table
        cursor.execute("SELECT * FROM Reservations WHERE reservation_month=%s AND reservation_day=%s AND reservation_time=%s AND reservation_technician=%s", (selectedMonth, selectedDay, selectedTime, technician))
        rows = cursor.fetchall()
        if(rows):
            print(""" """)
            print("""Someone has already scheduled an appointment with these attributes. Try a different time, day or technician""")
            time.sleep(2)
            x = 1
        else:
        ####Confirm reservation######
            while True:
                confirmation = input(f"""
                
                Reservation:
                Month: {selectedMonth} 
                Day: {selectedDay} 
                Time: {selectedTime} 
                Technician: {technician}
                Service: {selectedService} 
                >>>> Confirm this reservation ??? 
                
                1. Yes
                2. No
                
                >> """)
                if confirmation == "1":
                    # inserting info in reservation table
                    cursor.execute("""INSERT INTO Reservations (reservation_month, reservation_day, reservation_time, reservation_service,  reservation_technician, username)
                    VALUES (%s, %s, %s, %s, %s, %s)""", (selectedMonth, selectedDay, selectedTime, selectedService, technician, username)) 
                    conn.commit()
    
                    # inserting info in order table

                    cursor.execute("""INSERT INTO orders (username, servicename, service_price, processed_order) 
                    VALUES (%s, %s, %s, 'no')""", (username, selectedService, service_price)) 
                    conn.commit()
                    cursor.close()
                
                    print("Thank you for your business. We will see you soon...")
                    time.sleep(3)
                    break          
                elif confirmation == "2":
                    print("Re-schedule your appointment... ")
                    time.sleep(2)
                    reservation()
                    break
                else: 
                    print(" ")
                    print("Wrong answer. Select only '1' or '2' ")
                    time.sleep(2)


            
# cursor.execute("SELECT * FROM users WHERE username=%s AND user_pass=%s", (username, password))


    def myReservations():
        global username
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Reservations WHERE username='{username}'")
        rows = cursor.fetchall()
        counter = 1
        if(rows):
            for row in rows:
                print(" ")
                print(f"Reservation #{counter}")
                print(" ")
                print("Month= ", row[1])
                print("Day = ", row[2])
                print("Time = ", row[3])
                print("Service = ", row[4], "\n")
                counter+=1
            time.sleep(10)
               
        else:
            print(" ")
            print(f"{username}, You do not have any reservations.")
            time.sleep(3)
           
        cursor.close()
        x = 1




    subtotal = 0
    def myOrders():
        global username
        global subtotal
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Orders WHERE username=%s AND processed_order=false", (username,))
        rows = cursor.fetchall()
        counter = 1
        if(rows):
            for row in rows:
                print(" ")
                print(f"Order #{counter}")
                print(" ")
                print("Service= ", row[2])
                print("Price = ", row[3])
                print("Processed status = ", row[4], "\n")
                counter+=1
                subtotal += float(row[3][1:])
            time.sleep(2)

               
        else:
            print(f"{username}, you either have not made any reservations or have already paid for your order.")
            time.sleep(1)
            
        cursor.close()
        x = 1

    
    def paymentInfo():
        global username
        cursor = conn.cursor()
        cardName = input("Enter full name that is listed on your credit/debit card >> ")

        #credit card number validation
        cardNumberValid = False
        while(cardNumberValid == False):
            cardNumber = input("Enter your 16-digit credit/debit card number >> ")
            if(re.search("[a-zA-Z@_!#$%^&*()<>?/\|}{~:]", cardNumber) or len(cardNumber) != 16):
                print("")
                print("""Invalid credit/debit card number format. Please enter a valid 16-digit credit/debit card number.
                """)
            else:
                cardNumberValid = True

        #card expiration validation
        cardExpirationValid = False
        while(cardExpirationValid == False):
            cardExpiration = input("Enter your credit/debit card expiration date [mmyyyy] >> ")
            expireMonth = cardExpiration[0:2]
            expireYear = cardExpiration[2:]
            if((re.search("[a-zA-Z@_!#$%^&*()<>?/\|}{~:]", cardExpiration) or len(cardExpiration) != 6) or int(expireMonth) > 12 or int(expireYear) < 2019):
                print("")
                print("""Invalid credit/debit card expiration date. Please enter a valid 6-digit credit/debit card expiration date.
                """)
            else:
                cardExpirationValid = True

        #card security validation
        cardSecurityValid = False
        while(cardSecurityValid == False):
            cardSecurity = input("Enter your 3-digit credit/debit card security code >> ")
            if(re.search("[a-zA-Z@_!#$%^&*()<>?/\|}{~:]", cardSecurity) or len(cardSecurity) != 3):
                print("")
                print("""Invalid credit/debit card security code. Please enter a valid 3-digit credit/debit card security code.
                """)
            else:
                cardSecurityValid = True

        cursor.execute(f"INSERT INTO Payments(card_number, card_name, security_number, card_expiration, username) VALUES (%s, %s, %s, %s, %s)", (cardNumber, cardName, cardSecurity, cardExpiration, username,))
        cursor.execute(f'UPDATE Orders SET processed_order=true WHERE username=%s', (username,))
        conn.commit()
        cursor.close()

    def checkout():
        global subtotal
        subtotal = 0
        myOrders()
        print("")
        tax = subtotal * 0.07
        if(subtotal == 0):
            print("Please make a reservation before checking out.")
            time.sleep(3)
            x = 1
        else:
            print(f"""
            Subtotal......${subtotal}
            Tax...........${round(tax, 2)}
            Total.........${subtotal + tax}
            """)
            print("")
            while True:
                checkoutOption = input("Would you like to make a payment [y/n] >> ").lower()
                if(checkoutOption == "y"):
                    paymentInfo()
                    print("")
                    print("Payment successfully made. Thank you for your business!")
                    time.sleep(3)
                    subtotal = 0
                    x = 1
                    break
                elif(checkoutOption == "n"):
                    x = 1
                    subtotal = 0
                    break
                else:
                    print("Incorrect option, please try again.")

 
    
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from your database", error)

