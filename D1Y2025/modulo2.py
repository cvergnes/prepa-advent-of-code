
def main():
    instructions = []
    with open("puzzle", "r") as sample : 
        for line in sample :
            instructions.append(line)
    result = 50
    counter = 0
    for instruction in instructions: 
        prevResult = result
        if instruction[0] == 'R' : 
            result = (result + int(instruction[1:])) 
        elif instruction[0] == 'L' : 
            result = (result - int(instruction[1:]))
        if result == 0 : 
            counter += 1
        elif result < 0 :
            counter += abs((result-1)// 100) - (1 if prevResult == 0 else 0)
        elif result >= 100 : 
            counter += result // 100 
        result = (result % 100)
    print(counter)

main()
