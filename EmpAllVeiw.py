# EmpView.py <------Module Name
import pickle


def viewAllEmployees():
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

    print("=" * 55)
    print(f"{'ENO':<12} | {'NAME':<25} | {'SALARY':<12}")
    print("=" * 55)

    if not records:
        print("\tNo employee records found.")
    else:
        for record in records:
            eno, name, sal = record[0], record[1], record[2]
            print(f"{str(eno):<12} | {str(name):<25} | {sal:<12.2f}")

    print("=" * 55)





if __name__ == "__main__":
    viewAllEmployees()