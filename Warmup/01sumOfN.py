def sumOfN():
    N = int(raw_input())
    s = (raw_input())
    s = s.split(" ")
    sum=0
    for i in range(N):
        sum+=int(s[i])
    print sum
    