def sort_list(myList):
    n = len(myList)
    i = 0
    result = True
    for ele in myList:
        if not isinstance(ele, type(myList[0])):
            result = False
            break

    while i < n:
        j = 0
        while j < (n - i - 1):
            if result:
                if myList[j] > myList[j+1]:
                    myList[j], myList[j + 1] = myList[j + 1], myList[j]
                
            j = j + 1

        i = i + 1


    if result:
        return myList
    else:
        print('List is not valid')



