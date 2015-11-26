def angryProf():
    t = int(raw_input())
    for test_case in range(t):
        getN_and_K = raw_input()
        getN_and_K = map(int,getN_and_K.split(" "))
        n = getN_and_K[0]
        k = getN_and_K[1]
        arr = []
        arr = raw_input()
        arr = map(int, arr.split(" "))
        count = 0
        for i in range(n):
            if arr[i]<=0:
                count+=1
        if count < k:
            print "YES"
        else:
            print "NO"
                