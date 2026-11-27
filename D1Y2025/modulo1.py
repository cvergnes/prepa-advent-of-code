
def main():
    instructions = []
    with open("puzzle", "r") as sample : 
        for line in sample :
            instructions.append(line)
    result = 50
    counter = 0
    for instruction in instructions: 
        if instruction[0] == 'R' : 
            result = (result + int(instruction[1:])) 
        elif instruction[0] == 'L' : 
            result = (result - int(instruction[1:]))
        result = (result % 100)
        if result == 0 : 
            counter += 1        
    print(counter)

main()
