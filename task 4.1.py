from math import sqrt
def sqroots(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ("Unlim roots")
            return []
        return [-c/b]
    d = b**2 - (4*a*c)
    if d >= 0:
        return (-b-sqrt(d))/(2*a), (-b+sqrt(d))/(2*a)
    else:
        return []
def islegit(line):
    root = line.split("\t")
    try:
        a, b, c = [int(i) for i in root]
    except:
        return []
    else:
        return [a, b, c]
#abc = [][]
with open ("output.txt", "w") as output:
    
    with open("1.txt") as file:
        for line in file:
            row = islegit(line)
            if row:
                try:
                    out_root = sqroots(*row)
                    if len(out_root)  == 2:
                        output.write(f"{out_root[0]}, {out_root[1]}")
            except:
                    pass
            else:
                print("Incorrect input data")
