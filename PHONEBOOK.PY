import sys
def initial_phonebook():
    rows,cols = int(input("please enter initial number of contacts: ")), 5
    phonebook = []
    for i in range(rows):
        print("\nEnter contact %d details in the following oder(ONLY):"% (i+1))
        print("NoTe: * indicates mandatory field")
        print("......................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("enter name *: ")))
                if temp[j] == "" or temp[j] ==" ":
                    sys.exit("name is mandatory field. process exiting due to blank felid...")
            if j == 1:
                temp.append(int(input("enter number *: ")))
            if j == 2:
                temp. append(str(input("enter email address")))
                if temp[j] == "" or temp[j] ==" ":
                    temp[j] = None
