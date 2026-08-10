import pickle
def viewAllEmployees():
    with open("C:\\Employee_Project\\employee.data", "rb") as fp:
        print("---------------------------------------")
        print("\tENO\t\tNAME\t\tSALARY")
        print("---------------------------------------")
        while(True):
            try:
                record = pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("---------------------------------------")
                break

