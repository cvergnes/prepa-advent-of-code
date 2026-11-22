current = []
result= [0, 0, 0]
with open("puzzle", "r") as sample : 
    for line in sample :
        if line.strip() == "" :
            result = max(min(result), sum(current))
            current = []
        else : 
            current.append(int(line))
print(result)
