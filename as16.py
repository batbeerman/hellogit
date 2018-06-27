import MySQLdb
datab=MySQLdb.connect("localhost","root","2126","Database1")
cursor=datab.cursor()
#Q1

sl="""CREATE TABLE BOOKS BOOK_ID INT NOT NULL,
TITLE_ID INT,
LOCATION CHAR(20)
GENRE CHAR(20)
"""
s2="""CREATE TABLE TITLES TITLE_ID INT NOT NULL,
TITLE CHAR(20),
ISBN INT, 
PUBLISHER CHAR(20),
PUBLISHER_ID INT,
"""
s3="""SELECT * from BOOKS b JOIN TITLE t 
WHERE 
b.TITLE ID=t.TITLE ID
"""
cursor.execute(sl)
cursor.execute(s2)
cursor.execute(s3)

#Q2
sl="INSERT INTO BOOKS VALUES('%d', '%d', '%s', '%s') % (113, 212, "Lucknow","Comedy")
try:
    cursor.execute(sl)
    db.commit()
except:
    db.rollback()

#Q3
sl="SELECT * FROM BOOKS"
cursor.execute(sl)
s4="UPDATE BOOKS SET GENRE="Comedy" WHERE LOCATION="Madras"
try:
    cursor.execute(sl)
    db.commit()
except:
    db.rollback()
sl="SELECT * FROM BOOKS"
db.close()
