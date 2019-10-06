import psycopg2

try:
    conn = psycopg2.connect(
        database="Python_Project_ACD",
        user="postgres",
        password="MacBookPro",
        host="127.0.0.1",
        port="5432"
    )

    def insertUserInfo(fname, lname, phone, username, password, question1, question2):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO authentic (first_name, last_name, phone_number, username, user_password, sec_question1, sec_question2) VALUES ('{fname}', '{lname}', '{phone}', '{username}', '{password}', '{question1}', '{question2}')"
        )
        conn.commit()
        print("Record inserted successfully")
        cursor.close()

    fname = input("Enter name >> ")
    lname = input("Enter last name >> ")
    phone = input("Enter phone number >> ")
    username = input("Enter username >> ")
    password = input("Enter password > ")
    question1 = input("Please answer this security question: What is your middle name?")
    question2 = input("Please answer this security question: Where were you born?")

    insertUserInfo(fname, lname, phone, username, password, question1, question2)

    def insertReservationInfo(fname, lname, phone, month, day, time, service, tech):
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO reservation (first_name, last_name, phone_number, month_sch, day_sch,time_sch, service_sch, technician) VALUES ('{fname}', '{lname}', '{phone}', '{month}', '{day}', '{time}', '{service}', '{tech}')"
            )
            conn.commit()
            print("Record inserted successfully")
            cursor.close()

        fname = input("Enter name >> ")
        lname = input("Enter last name >> ")
        phone = input("Enter phone number >> ")
        month = input("Enter month >> ")
        day = input("Enter day > ")
        time = input("Enter time?")
        service = input("Enter service")
        tech = input("Enter Technician name")

        insertReservationInfo(fname, lname, phone, month, day, time, service, tech)

except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)