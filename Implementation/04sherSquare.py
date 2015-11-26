from math import sqrt,floor,ceil
def sherSquare():
    for t in range(int(raw_input())):
        getAandB = map(int,raw_input().split(" "))
        a = getAandB[0]
        b = getAandB[1]
        if a <= b:
            print int( floor(sqrt(b)) - ceil(sqrt(a)) + 1 )
                 
        