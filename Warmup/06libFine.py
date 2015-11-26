def libFine():
    actual_date = raw_input()
    actual_date = map(int,actual_date.split(" "))
    exp_date = raw_input()
    exp_date = map(int, exp_date.split(" "))
    
    if actual_date[2] < exp_date[2]:
        print 0
    elif actual_date[1] < exp_date[1] and actual_date[2] <= exp_date[2]:
        print 0
    elif actual_date[0] <= exp_date[0] and actual_date[1] <= exp_date[1] and actual_date[2] <= exp_date[2]:
        print 0
    elif actual_date[0] > exp_date[0] and actual_date[1] <= exp_date[1] and actual_date[2] <= exp_date[2]:
        print 15*( actual_date[0] - exp_date[0])
    elif actual_date[1] > exp_date[1] and actual_date[2] <= exp_date[2]:
        print 500*( actual_date[1] - exp_date[1])
    elif actual_date[2] > exp_date[2]:
        print 10000