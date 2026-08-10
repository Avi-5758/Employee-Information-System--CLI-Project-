#addEmp.py
import pickle
def addEmployee():
    try:
        with open("C:\\Employee_Project\\employee.data","ab") as file:
            empno = int(input("Enter Employee Number: "))
            empname = input("Enter Employee Name: ")
            empsal = int(input("Enter Employee Salary₹: "))
            lst = []
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            pickle.dump(lst,file)
            print("Employee Added Successfully!")
    except ValueError:
            print("Please Only Integer Value")



addEmployee()
