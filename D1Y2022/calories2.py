current = []
result= [0, 0, 0]
with open("puzzle", "r") as sample : 
    for line in sample :
        print(line.strip())
        if line.strip() == "" :
            result.append(sum(current))
            result.sort()
            result = result[1:]
            current = []
        else : 
            current.append(int(line))
print(result)            
print(sum(result))
