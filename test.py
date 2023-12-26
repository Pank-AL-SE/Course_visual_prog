import sqlite3
db = sqlite3.connect('people.db')
c = db.cursor()


#create
# c.execute("""
#       CREATE TABLE employee (
#             Data text,
#             FIO text,
#             ser text,
#             num text,
#             dateof_v text,
#           which_place text,
#           pace_live text,
#             work text,
#           price text,
#           med)
#   """)

# c.execute("""
#       CREATE TABLE history (
#             Data text,
#             FIO text,
#             work text,
#             status text
         
# )
#   """)
# c.execute("""
#       CREATE TABLE not_employee (
#             Data text,
#             FIO text,
#             ser text,
#             num text,
#             dateof_v text,
#           which_place text,
#           pace_live text,
#             work text,
#           reason text,
#           med)
#   """)

#ADD
#c.execute("INSERT INTO workers VALUES('1','test','test','test','test')")

#change
#c.execute("UPDATE workers SET num = '0' WHERE rowid = 1 ")

#find from * we can put name of titles <>
#c.execute("SELECT * FROM employee")

#c.execute("DELETE FROM employee")

#choose all print
print(c.fetchall())

#save
db.commit()
db.close()