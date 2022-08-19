myList = []
c = "y"
while c=="y":
    print("1.Add Element")
    print("2.Delete Element")
    print("3.Display The Elements")
    print("4.Find the INDEX of an ELEMENT")
    print("5.Exit")
    
    choice = int(input("Enter your Choice : "))
    if choice ==1:
        times = int(input("How many elements you want to enter ? "))
        for i in range(times):
            element = input("Enter the element: ")
            myList.append(element)

    elif choice ==2:
        if myList ==[]:
            print("LIST is EMPTY ! Cannot DELETE from an EMPTY list !!")
        else:
            print(myList)
            eleName = input("Enter the name of the element : ")
            myList.remove(eleName)
            print("The element ",eleName,"has been DELETED !")

    elif choice == 3:
        if myList ==[]:
            print("LIST is EMPTY !!")
        else:
            print(myList)

    elif choice == 4:
        if myList ==[]:
            print("LIST is EMPTY !!")
        else:
           print(myList)
           element = input("Enter the element to find its INDEX : ")
           length = len(myList)
           for i in range(length):
               if element == myList[i]:
                   print("The index of the element ",element,"is ",i)
               else:
                   pass

    elif choice ==5:
        break

    else:
        print("INVAILD INPUT !!")

    c = input("Do you want to contine ? Press y to continue ! ")
print("The Program is TERMINATED !")     




