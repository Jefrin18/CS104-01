#List creation and searching
names  = []
for x in range (0,10):
    aName = input ("Enter Name")
    names.append(aName)
searching = True

while searching is True:
    print (names)
    search = input("enter search name:")
    if search in names:
        print(search, "was found")
        answer = str(input("Search for a different name?"))
        if answer == "No" or answer == "no":
            print("System Closed")
            break
        elif answer == "Yes" or answer == "yes":
            continue
        else:
            print (search, "was not found")
            answer = str(input("Search for a different name?"))
            if answer == "No" or answer == "no":
                print("System Closed")
                break
            elif answer == "Yes" or answer == "yes":
                continue
