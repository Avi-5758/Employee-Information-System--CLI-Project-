#EmpSearch.py <-------Module Name
import pickle as pkl
def employeeser():

    records=[]
    with open("C:\\Employee_Project\\employee.data", "rb") as fp:
        while True:
            try:
                record = pkl.load(fp)
                records.append(record)
            except EOFError:
                break
            empno = int(input("Enter Employee Number: "))  # Add int() here
            found=False
            for record in records:
                if (str(record[0]) == str(empno)):
                    found=True
                    break
            print("-"*50)
            if found:
                print("\tValid Employee ")
            else:
                print("\tInvalid Employee ")
            print("-"*50)




