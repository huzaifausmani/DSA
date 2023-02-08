def findMissing(sortedList, size):
    for i in range(1, size):
        if i not in sortedList:
            return i
        if size-i not in sortedList:
            return size-i
        

sortedList = [9,2,4,6,3,8,7,1]
print(findMissing(sortedList, len(sortedList)))
    
    