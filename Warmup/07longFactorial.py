def largeFact():
    n = int(raw_input())
    prod = 1
    for i in range(1,n+1):
        prod*=i
    print prod