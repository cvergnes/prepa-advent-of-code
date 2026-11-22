list1 = []
dico2 = {}
result = 0
with open("puzzle", "r") as sample : 
    for line in sample :
        one, two = line.split()
        list1.append(int(one))
        if int(two) in dico2 :
           dico2[int(two)] += 1
        else :
           dico2[int(two)] = 1
for item in list1: 
    if item in dico2 :
        result += item*dico2[item]
print(result)
