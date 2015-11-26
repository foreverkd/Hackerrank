def diagonalDiff():
    n = int(raw_input())
    matrix = []
    for i in range(0,n):
        matrix.append([])
        for j in range(0,n):
            matrix[i].append(0)
    for i in range(0,n):
        s = raw_input()
        s = map(int,s.split(" "))
        print s
        for j in range(n):
            matrix[i][j] = s[j]
    sum1=sum2=0
    for i in range(n):
        sum1+=matrix[i][i]
    print sum1
    for i in range(n):
        sum2+=matrix[i][n-i-1]
    print sum2    
    print abs(sum1-sum2)
    
    