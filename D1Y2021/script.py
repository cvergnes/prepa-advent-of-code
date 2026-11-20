prev = None
counter = 0
with open("puzzle1", "r") as puzzle1 : 
    for line in puzzle1 :
        if prev != None and int(prev) < int(line) :
            counter += 1
        prev = int(line)
print(counter)
