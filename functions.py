import psycopg2, time
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
        print("")
        print("""****** NEW USER REGISTRATION ******
        """)

        fName = raw_input("Enter your first name >> ")
        lName = raw_input("Enter your last name >> ")        
        phone = raw_input("Enter your phone number >> ")        
        username = raw_input("Enter your username >> ")        
        password = raw_input("Enter your password >> ")        
        userAddress = raw_input("Enter your home address >> ")        
        zipCode = raw_input("Enter your zip code >> ")        
        answer1 = raw_input("What is your middle name? >> ")     
        answer2 = raw_input("Where were you born? >> ")

        cursor.execute("""INSERT INTO users (First_name, Last_name, phone_number, Username, User_pass, User_address, Zip_code, Answer1, Answer2) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (fName, lName, phone, username, password, userAddress, zipCode, answer1, answer2)
        )

        print("Welcome, " + fName)
        time.sleep(2)

        conn.commit()
        cursor.close()

     
    

#Authentication (I'm using raw_input command because I have an older python version. I haven't been able to solve this)
  

    def auth(): 
        username= raw_input("Username: ")
        password= raw_input("Password: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND user_pass=%s", (username, password))
        rows = cursor.fetchall()
        # file = open("log.txt", 'a' )
        # now = datetime.datetime.now()
        if(rows):
            print("You have succesfully logged in!")
            # file.write(f"User {username} loged in at {now}\n")
        else:
            print("Wrong credentials")
            # file.write(f"Some tried to login using this username '{username}' at {now}\n")
            # file.close()
        cursor.close()
 
    
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from your database", error)

