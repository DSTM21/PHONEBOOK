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
                temp. append(str(input("enter email address: ")))
                if temp[j] == "" or temp[j] ==" ":
                    temp[j] = None
            if j == 3:
                temp.append(str(input("enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j]== "":
                    temp[j] = None
            if j == 4:
                temp.append(input("enter category (family/freinds/work others):"))
                if temp[j] == "" or temp[j] ==" ":
                    temp[j] = None
        phonebook.append(temp)
    
    print(phonebook)
    return phonebook
def menu():
    print("**********************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("**********************************************")
    print("\tYou can now perform the following operations on this phonebookt\n")
    print("1. Add a new contact")
    print("2. Remove  an existing contact")
    print("3. Delete all contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("plz enter your choice: "))
    return choice
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("enter name: ")))
        if i == 1:
            dip.append(int(input("enter number: ")))
        if i == 2:
            dip.append(str(input("enter email address: ")))
        if i == 3:
            dip.append(str(input("enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(input("enter category (family/friends/work/others): "))
    pb.append(dip)
    return
