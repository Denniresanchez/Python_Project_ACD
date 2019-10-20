import psycopg2, datetime, time, functions, os

# While loop Registered or not?
x = 1
while x == 1:
    os.system('clear')
    answer = input("Are you a New User? (Y/N) -->> ").upper()
    if answer != 'Y' and answer != 'N':
        print("""
        
        I am sorry, that is not a valid option. Try again...""")
        time.sleep(3)
        os.system('clear')
    
    elif answer == 'Y':
        functions.newUser()
        x = 0
    
    elif answer == 'N':
        functions.auth()
        x = 0
            
    #while loop to see the main menu
x = 1
while x == 1:
    os.system('clear')
    print(""" 
    
    **** PLEASE SELECT AN OPTION: **** 

    1. Make a Reservation
    2. Check out
    
    """)
    selection = input("Select an option >> ")
    if selection != "1" and selection != "2":
        print(" ")
        print("""
        
        Invalid option, select a valid option in the menu.""")
        time.sleep(2)
        x = 1
    if selection == "1":
        print(" ")
        functions.reservation()
        
        x = 0
    if selection == "2":
        print("checkout")
        x = 0 
        


# except (Exception, psycopg2.Error) as error:
#     print("Error while fetching data PostgreSQL", error)