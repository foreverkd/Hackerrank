def serviceLane():
    TandN = map(int,raw_input().split(' '))
    n = TandN[0]
    t = TandN[1]
    arr = map(int,raw_input().split(' '))
    for i in range(t):
        seg = map(int,raw_input().split(' '))
        print seg[0], seg[1]
        print min(arr[seg[0]:seg[1]+1])
         
    