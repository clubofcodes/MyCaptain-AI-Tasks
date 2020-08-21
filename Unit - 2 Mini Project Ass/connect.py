import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.connection = sqlite3.connect("emp.db")
            # print("DB created")
            self.connection.execute('''create table if not exists employee(
                  emp_name text,
                  email text,
                  mobile text,
                  emp_type char,
                  emp_salary integer,
                  emp_exp integer
            )''')
            self.connection.commit()
            self.connection.close()
            #5      
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6

      def display(self):
            #7