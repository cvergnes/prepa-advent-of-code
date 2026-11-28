
def main():
    inter = []
    products = []
    with open("puzzle", "r") as sample : 
        for line in sample :
            if "-" in line : 
                inter.append(list(map(int, line.split("-"))))
            elif line.strip() != "" :
                products.append(int(line))
    intervals = sorted(inter, key=lambda item: item[0])

    result = [intervals[0]]
    prev_start, prev_end = result[0][0], result[0][1]
    for interval in intervals[1:] :
        if interval[0] <= prev_end +1 :
            result[-1] = [ prev_start, max(interval[1], prev_end) ]
        else :
            result.append([ interval[0], interval[1]])
        
        prev_start, prev_end = result[-1][0], result[-1][1]

    counter = 0
    for interval in result : 
        counter += interval[1] + 1 - interval[0]

    print(counter)

main()
