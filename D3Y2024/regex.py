import re 

str = ""
with open("puzzle", "r") as sample : 
    for line in sample :
        str += line

result = 0
active = True
match = re.finditer(r'mul\(([\d]+),([\d]+)\)|do\(\)|don\'t\(\)', str)
for m in match :
    token = m.group(0)
    if token == "do()":
        active = True
    elif token == "don't()":
        active = False
    elif active:
        a, b = map(int, m.groups())
        result += a * b
print(result)


