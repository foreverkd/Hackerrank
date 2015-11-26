def chocoFeast():
    T = int(raw_input())
    for i in range (0,T):
        A,B,C1 = [int(x) for x in raw_input().split(' ')]
        ord
        answer = 0
        # write code to compute answer
        num = A/B
        answer+=num
        while num >= C1:
            if num == C1:
               answer+=1
               num-=C1
            else:
                answer+=1
                num= num - C1+1
            
        print answer
    