
def main():
    intervals = []
    products = []
    with open("puzzle", "r") as sample : 
        for line in sample :
            if "-" in line : 
                intervals.append(list(map(int, line.split("-"))))
            elif line.strip() != "" :
                products.append(int(line))
    sorted(intervals, key=lambda item: item[1]-item[0], reverse= True)
    counter = 0
    for product in products : 
        for interval in intervals : 
            if product <= interval[1] and product >= interval[0] :
                counter += 1
                break


    print(counter)

main()
