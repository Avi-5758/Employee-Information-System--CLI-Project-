import pickle
def viewSingleEmployee():
    records = []
    try:
        with open("C:\\Employee_Project\\employee.data", "rb") as fp:
            while True:
                try:
                    records.append(pickle.load(fp))
                except EOFError:
                    break
    except FileNotFoundError:
        print("\nData file not found.")
        return
    print("-" * 50)
    empno = input("Enter Employee Number to Search: ").strip()
    found = False
    for record in records:
        if str(record[0]) == str(empno):
            print("\nMatch Found:")
            print("-" * 35)
            print(f"  Employee ID   : {record[0]}")
            print(f"  Name          : {record[1]}")
            print(f"  Salary        : ₹{record[2]:,.2f}")
            print("-" * 35)
            found = True
            break

    if not found:
        print("\tEmployee Number Not Found")
    print("-" * 50)

#Main program.
viewSingleEmployee()
