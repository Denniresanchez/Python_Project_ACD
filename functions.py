import psycopg2, datetime

try:
    # required information to use the db 
    conn = psycopg2.connect(
        database = "investor", # database name
        user = "postgres",
        password = "6108", #your password
        host = "127.0.0.1",
        port = "5432"
    )
    
    def authentication(): 
        cursor = conn.cursor()
        username = input("Username: ")
        password = input("Password: ")
        cursor.execute(
            f"""SELECT * FROM accounts WHERE username='{username}' and user_pass='{password}'"""
        )
        conn.commit()
        rows = cursor.fetchall()
        cursor.close()

        file = open("log.txt", 'a' )
        now = datetime.datetime.now()
        if rows:
            print("Athentication succesfull!")
            file.write(f"User {username} loged in at {now}\n")
        else:
            print("Wrong credentials")
            file.write(f"Some tried to login using this username '{username}' at {now}\n")

        file.close()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)