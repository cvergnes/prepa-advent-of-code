
def main():
    str = ""
    with open("puzzle", "r") as sample : 
        for line in sample :
            str += line
    for i in range(len(str)-14):
        length = len(set(list(str[i:i+14])))
        if length == 14 :
            print(i+14)
            return

main()
