import sys
def pivot(n):
    while n>0:
        if n%3 == 0:
            break
        else:
            n-=5
    return n
    
def decentNo():
    t = int(raw_input())
    for test_case in range(t):
        n = int(raw_input())
        
        new_n = pivot(n)
        
        if new_n < 0:
            print '-1'
        else:
            repeat = new_n/3
            while repeat > 0:
                sys.stdout.write('555')
                repeat-=1
            repeat = (n-new_n)/5
            while repeat > 0:
                sys.stdout.write('33333')
                repeat-=1
            print ''
                
        