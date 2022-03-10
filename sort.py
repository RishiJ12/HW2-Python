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



list = [1,3,6,3,8,2,5,0,]
sort_list(list)
for num in list:
    print(num)



