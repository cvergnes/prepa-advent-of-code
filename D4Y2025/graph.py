
def main():
    grid = []
    with open("puzzle", "r") as sample : 
        for line in sample :
            grid.append(list(line))
    prevResult = -1
    result = 0
    while prevResult != result : 
        prevResult = result
        for i in range(len(grid)):
            for j in range(len(grid)):
                count = 0
                if grid[i][j] != '@':
                    continue
                if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == '@' :
                    count += 1
                if i-1 >= 0 and grid[i-1][j] == '@' :
                    count += 1
                if i-1 >= 0 and j+1 < len(grid) and grid[i-1][j+1] == '@' :
                    count += 1
                if j-1 >= 0 and grid[i][j-1] == '@' :
                    count += 1
                if j+1 < len(grid) and grid[i][j+1] == '@' :
                    count += 1
                if i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == '@' :
                    count +=1
                if i+1 < len(grid) and grid[i+1][j] == '@' :
                    count +=1
                if i+1 < len(grid) and j+1 < len(grid) and grid[i+1][j+1] == '@' :
                    count +=1
                if count < 4 :
                    result += 1
                    grid[i][j] = 'x'
    print(result)

main()
