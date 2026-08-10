#EmpDelete.py<--Module Name
import pickle
def deleteEmployee():
    # get all the records for Viewing single Employee Deatils Based on ENO
    records = []  # Outer List
    with open("C:\\Employee_Project\\employee.data", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get Employee Number for Removing the Record
    print("-"*50)
    found=False
    try:

        empno=int(input("Enter Employee Number to Delete:"))
        for record in records:
            if(str(record[0])==str(empno)):
                rec=record
                found=True
                break
    except ValueError:
        print("\t Enter Only Numeric Value")
    if(found):
        records.remove(rec)
        #Re-write the Remaining Records to File after delete
        with open("C:\\Employee_Project\\employee.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Deleted--Verify")
    else:
        print("\tEmployee Number Not Found")
    print("-"*50)


deleteEmployee()

