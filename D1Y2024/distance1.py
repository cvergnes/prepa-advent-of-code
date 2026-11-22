list1 = []
list2 = []
result = 0
with open("puzzle", "r") as sample : 
    for line in sample :
       one, two = line.split()
       list1.append(int(one))
       list2.append(int(two))

list1.sort()
list2.sort()
for i in range(len(list1)): 
    result += abs(list1[i] - list2[i])
print(result)
