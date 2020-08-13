import sqlite3
import re
class myconnect:
    def __init__(self):
        self.connection = sqlite3.connect("employee.db")
        # print("DB created")
        self.connection.execute('''create table if not exists emp(
            emp_name text,
            email text,
            mobile text,
            j_type text,
            emp_salary integer,
            emp_exp integer
        )''')
        self.connection.commit()
        self.connection.close()
    def insert(self,e):
        pattern = re.compile(r"M[.A-Za-z0-9-]+\D\S+")
        if(pattern.search(e.email)):
            self.connection=sqlite3.connect("employee.db")
            self.connection.execute("insert into emp values(?,?,?,?,?,?)",(e.emp_name,e.email,e.mobile,e.j_type,e.emp_salary,e.emp_exp))
            self.connection.commit()
            self.connection.close()
        else:
            print("Enter Valid Email address... \n")
            return
    def display(self,id):
        self.connection=sqlite3.connect("employee.db")
        print("Your Name : ",self.connection.execute("select * from emp").fetchall()[id-1][0])
        print("Your Email :",self.connection.execute("select * from emp").fetchall()[id-1][1])
        print("Your Contact Number :",self.connection.execute("select * from emp").fetchall()[id-1][2])
        print("Your Job-Type : ",self.connection.execute("select * from emp").fetchall()[id-1][3])
        print("Your Salary : ",self.connection.execute("select * from emp").fetchall()[id-1][4])
        print("Your Work Experirence",self.connection.execute("select * from emp").fetchall()[id-1][5])
        print("\n")
        self.connection.commit()
        self.connection.close()