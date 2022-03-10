def sort_list(myList):
    n = len(myList)
    i = 0
    while i < n:
        j = 0
        while j < (n - i - 1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

            j = j + 1
            
        i = i + 1
                
    return myList




