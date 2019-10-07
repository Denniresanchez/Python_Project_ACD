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
    
#While loop Registered or not?
counter = 1
while counter = 1
    answer = input("Are you a New User? -->> (Y/N)").upper()
    if answer != Y and answer != N:
        print("I am sorry, that is not a valid option. Try again...")
        counter = 1
    elif answer = Y:
        newUser()
        counter = 0
    elif answer = N:
        auth()
        counter = 0
        
















except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)