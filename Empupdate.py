# EmpUpdate.py<--Module Name
import pickle
def updateEmployee():
    # get all the records for Viewing single Employee Details Based on ENO
    records = []  # Outer List
    try:
        with open("C:\\Employee_Project\\employee.data", "rb") as fp:
            while True:
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("\nData file not found.")
        return
    # Get the Records
    print("-" * 50)
    found = False
    recindex = -1
    try:
        empno = int(input("Enter the Employee Number to Update Salary: "))
        for index in range(len(records)):
            if str(records[index][0]) == str(empno):
                recindex = index
                found = True
                break
    except ValueError:
        print("\tEnter Only Integer Value")
    if found:
        try:
            newsal = float(input("Enter the New Salary: "))
            records[recindex][2] = newsal
            # Re-write Modified Records to the File
            with open("C:\\Employee_Project\\employee.data", "wb") as fp:
                for record in records:
                    pickle.dump(record, fp)
            print("\tEmployee Salary Updated--verify")
        except ValueError:
            print("\tInvalid Salary! Enter numbers only.")
    else:
        print("\tEmployee Number Not Found")
    print("-" * 50)

#Main program
    updateEmployee()