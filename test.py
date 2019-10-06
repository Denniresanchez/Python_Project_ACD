import psycopg2

try:
    conn = psycopg2.connect(
        database="Python_Project_ACD",
        user="postgres",
        password="MacBookPro",
        host="127.0.0.1",
        port="5432"
    )

    name = input('name')


    # name = input("Enter name >> ")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO authentication (first_name, last_name, phone_number, username, user_password, sec_question_1, sec_question_2) 
            VALUES ({}, 'neptuno', '18000', 'elmaschido', 'asdasd', 'asd', 'asdasd')""".format(name))
    conn.commit()
    cursor.close()

    

except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)