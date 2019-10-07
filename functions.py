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
    
    username = ''
    password = ''
 
    username= raw_input("Username: ")
  
    password= raw_input("Password: ")

    def auth(user,passW): 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND user_pass=%s", (user, passW))
        rows = cursor.fetchall()
        # file = open("log.txt", 'a' )
        # now = datetime.datetime.now()
        if(rows):
            print("Athentication succesfull!")
            # file.write(f"User {username} loged in at {now}\n")
        else:
            print("Wrong credentials")
            # file.write(f"Some tried to login using this username '{username}' at {now}\n")
            # file.close()
        cursor.close()

    auth(username, password)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from your database", error)