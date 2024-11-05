# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Created Successfully')

# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')uo
# connect.execute(''' CREATE TABLE CUSTOMERS
#     (ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     AGE INT NOT NULL,
#     ADDRESS CHAR (100))
# ''')

# print('Table Created Successfully')

# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')

# connect.execute('''INSERT INTO CUSTOMERS
#     (ID, NAME, AGE, ADDRESS) \
#     VALUES(1, 'jOHN', 21, 'IKORODU')''')

# connect.commit()
# print('record added successfully')
# connect.close()


# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')

# connect.execute('''INSERT INTO CUSTOMERS
#     (ID, NAME, AGE, ADDRESS) \
#     VALUES(2, 'Jane', 19, 'KETU')''')

# connect.commit()
# print('record added successfully')
# connect.close()

# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')

# cursor = connect.execute("SELECT * FROM CUSTOMERS")
# for row in cursor:
#     print ("ID = ", row[0])
#     print ("NAME = ", row[1])
#     print ("AGE = ", row[2])
#     print ("ADDRESS = ", row[3])
    
# print('OPERATION COMPLETED SUCCESSFULLY')


# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')

# connect.execute("UPDATE CUSTOMERS set ADDRESS = 'IKEJA' where ID = 1")
# connect.commit()
# print('Record Updated' , connect.total_changes)


# import sqlite3

# connect= sqlite3.connect('databse.db')
# print('Databse Opened Successfully')

# connect.execute("DELETE from CUSTOMERS where ID = 2")
# connect.commit()
# print('Record deleted successfully', connect.total_changes)











