def plusMinus():
    n = int(raw_input())
    arr = raw_input()
    arr = map(int,arr.split(" "))
    print arr
    count1=count2=count3=0
    for i in range(n):
        if arr[i] > 0:
            count1+=1
        elif arr[i] < 0:
            count2+=1
        else:
            count3+=1
   
    print '%3f' % (float(count1)/float(n))
    print float(count2)/float(n)
    print float(count3)/float(n)