def findDigits():
    for t in range(int(raw_input())):
        n = int(raw_input())
        digits = []
        x = n
        while x > 0:
            digits.append(x%10)
            x/=10
        count = 0
        for digit in digits:
            if digit != 0:
                if n%digit == 0:
                    count+=1
        print count
                
            