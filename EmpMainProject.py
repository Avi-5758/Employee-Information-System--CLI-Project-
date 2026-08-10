#EmpMainProject.py
from unittest import case

from EmpMenu import menu
from addEmp import addEmployee
from EmpDelete import deleteEmployee
from Empupdate import updateEmployee
from EmpView import viewSingleEmployee
from EmpAllVeiw import viewAllEmployees
from EmpSearch import employeeser


while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addEmployee()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployees()
            case 6:
                employeeser()
            case 7:
                print ("Thank you for choosing This Project!!!")
                exit()
            case _:
                print("\t UR Selection of Operations is Wrong -Try - Again!!!")
    except ValueError:
        print("\t Please Enter Only Integer's")