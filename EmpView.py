#EmpView.py<--Module Name
import pickle
def viewSingleEmployee():
    #get all the records for Viewing single Employee Deatils Based on ENO
    records=[] # Outer List
    with open("C:\\Employee_Project\\employee.data","rb") as fp:
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    empno = int(input("Enter Employee Number:"))
    found=False
    for record in records:
        if(record[0]==empno):
            rec=record
            found=True
            break
    print("-"*50)
    if(found):
        print("\tEmployee Number:{}".format(rec[0]))
        print("\tEmployee Name:{}".format(rec[1]))
        print("\tEmployee Salary:{}".format(rec[2]))
    else:
        print("\tEmployee Number Does Not Exist")
    print("-" * 50)



