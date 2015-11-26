import sys
def staircase():
    n = int(raw_input())
    for i in range(n):
        for j in range(n-i-1):
            sys.stdout.write(' ')
        for k in range(i+1):
           sys.stdout.write('#')
        print