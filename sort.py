def sort_list(myList):
    n = len(myList)
    i = 0
    valid = True

    
    while i < n:
        j = 0
        while j < (n - i - 1):

            if myList[j] > myList[j+1]:
                if isinstance(myList[j], int) and isinstance(myList[j+1], int):
                    myList[j], myList[j + 1] = myList[j + 1], myList[j]
                else:
                    valid = False

            j = j + 1

        i = i + 1


    if valid:
        return myList
    else:
        print('List is not valid')




