import psycopg2, datetime, time, functions, os

print("""

 _______       .-''-.     ____      ___    _ ,---------. .-./`)  ________   ___    _   .---.                .-'''-. .-------.    ____            
\  ____  \   .'_ _   \  .'  __ `. .'   |  | |\          \\ .-.')|        |.'   |  | |  | ,_|               / _     \\  _(`)_ \ .'  __ `.         
| |    \ |  / ( ` )   '/   '  \  \|   .'  | | `--.  ,---'/ `-' \|   .----'|   .'  | |,-./  )              (`' )/`--'| (_ o._)|/   '  \  \        
| |____/ / . (_ o _)  ||___|  /  |.'  '_  | |    |   \    `-'`"`|  _|____ .'  '_  | |\  '_ '`)           (_ o _).   |  (_,_) /|___|  /  |        
|   _ _ '. |  (_,_)___|   _.-`   |'   ( \.-.|    :_ _:    .---. |_( )_   |'   ( \.-.| > (_)  )            (_,_). '. |   '-.-'    _.-`   |        
|  ( ' )  \'  \   .---..'   _    |' (`. _` /|    (_I_)    |   | (_ o._)__|' (`. _` /|(  .  .-'           .---.  \  :|   |     .'   _    |        
| (_{;}_) | \  `-'    /|  _( )_  || (_ (_) _)   (_(=)_)   |   | |(_,_)    | (_ (_) _) `-'`-'|___         \    `-'  ||   |     |  _( )_  |        
|  (_,_)  /  \       / \ (_ o _) / \ /  . \ /    (_I_)    |   | |   |      \ /  . \ /  |        \         \       / /   )     \ (_ o _) /        
/_______.'    `'-..-'   '.(_,_).'   ``-'`-''     '---'    '---' '---'       ``-'`-''   `--------`          `-...-'  `---'      '.(_,_).'  


""")



print("""

2600 SW 8th Street
Miami, Fl, 33135
786-360-1018
beautifulspamiami@gmail.com

OPEN
Monday to Sunday, 8:00 AM to 5:00 PM
Lunch break, 12:00 M to 1:00 PM 
""")

time.sleep(4)

# While loop Registered or not?
x = 1
while x == 1:
    os.system('clear')
    answer = input("Are you a New User? (Y/N) -->> ").upper()
    if answer != 'Y' and answer != 'N':
        print("""I am sorry, that is not a valid option. Try again...""")
        time.sleep(3)
        os.system('clear')
    
    elif answer == 'Y':
        functions.newUser()
        x = 0
       
    
    elif answer == 'N':
        if functions.auth():
            break 

        else:
            x = 1
       
            
    #while loop to see the main menu
x = 1
while x == 1:
    os.system('clear')
    print(""" 
    
    **** PLEASE SELECT AN OPTION: **** 

    1. Make a Reservation
    2. Check out
    3. See my Reservations
    4. See my orders
    5. Exit

    
    """)
  
    selection = input("Select an option >> ")
    if selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "5":
        print(" ")
        print("""Invalid option, select a valid option in the menu.""")
        time.sleep(2)
        x = 1
    elif selection == "1":
        print(" ")
        functions.reservation()
       
    elif selection == "2":
        functions.checkout()
  
    elif selection == "3":
        functions.myReservations()
      

    elif selection == "4":
        functions.myOrders()
       

    elif selection == "5":
        print("Bye....")
        time.sleep(2)
        x = 0