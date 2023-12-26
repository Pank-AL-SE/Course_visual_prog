import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()

    def save(self,date,a,b,c,d,e,f,g,h,i):
        self.db = sqlite3.connect('people.db')
        self.curs = self.db.cursor()
        self.curs.execute("INSERT INTO employee VALUES('"+date+"','"+a+"','"+str(b)+"','"+str(c)+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+str(i)+"')")
        self.curs.execute("INSERT INTO history VALUES('"+date+"','"+a+"','"+g+"','Устроен')")
        self.db.commit()
        self.db.close()

    def save_end(self,date,a,b,c,d,e,f,g,h,i):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()
        self.curs.execute("INSERT INTO not__employee VALUES('"+date+"','"+a+"','"+str(b)+"','"+str(c)+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+str(i)+"')")
        self.curs.execute("DELETE FROM employee WHERE FIO = '"+a+"'")
        self.curs.execute("INSERT INTO history VALUES('"+date+"','"+a+"','"+g+"','Уволен')")
        self.db.commit()
        self.db.close()

    
    def find_FIO(self,a):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM employee WHERE FIO = '"+a+"'")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check
    
    def find_place_live(self,a):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM employee WHERE place_live = '"+a+"'")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check
    
    def find_work(self,a):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM employee WHERE work = '"+a+"'")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check
    
    def find_price(self,a):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM employee WHERE price = '"+a+"'")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check
    
    def print_db(self):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM employee")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check
    def print_hist(self):
        self.db = sqlite3.connect('../coursevisualka/people.db')
        self.curs = self.db.cursor()        
        self.curs.execute("SELECT * FROM history")
        check = self.curs.fetchall()
        self.db.commit()
        self.db.close()
        return check



    def close(self):
        self.db.close()
