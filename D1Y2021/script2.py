prevSum = None
counter = 0
currentArr = []
with open("puzzle1", "r") as puzzle1 : 
    for line in puzzle1 :
        if len(currentArr) < 3 : 
            currentArr.append(int(line))
        else : 
            currentArr = currentArr[1:] + [int(line)]  
        if len(currentArr) == 3 and prevSum is not None and sum(currentArr) > prevSum :
            counter += 1
        if len(currentArr) == 3 : 
            prevSum = sum(currentArr)
print(counter)
