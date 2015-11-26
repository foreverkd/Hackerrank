def cutSticks():
    n = int(raw_input())
    arr = map(int,raw_input().split(' '))
    arr.sort()
    small = arr[0]
    print n
    for i in range(n):
         if arr[i] > small:
             small = arr[i]
             print n-i
