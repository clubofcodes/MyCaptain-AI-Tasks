from Connect import myconnect
class Employee:
    def __init__(self,emp_name=None,email=None,mobile=None,j_type=None,emp_exp=None,emp_salary=None):  #j_type=job type
        self.emp_name = input("Enter your Name : ")
        self.email = input("Enter your Email : ")
        self.mobile = input("Enter your Mobile No : ")
        self.j_type = input("Enter your Job Type : ")
        self.emp_exp = input("Enter your Experience : ")
        self.emp_salary = input("Enter your Salary :")

print("1. Add Employee")
print("2. Display Employee")
print("3. Add Notes")
print("4. Exit\n")
ch=int(input("Enter your choice : "))
while(ch!=4):
    if ch == 1:
        e = Employee()
        c = myconnect()
        c.insert(e)
    elif ch == 2:
        id = int(input("Enter ID "))
        c = myconnect()
        c.display(id)
    else:
        print("Come Tommorow")
    ch = int(input("Enter Your Choice : "))