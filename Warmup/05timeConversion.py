import re
def timeConversion():
    time = raw_input()
    match = re.search( r'(\d\d).*(\D\D)',time)
    
    if match:
        if match.group(2) == 'AM':
            x = int(match.group(1)) 
            if x == 12:
                new_x = '00'
            else:
                new_x = match.group(1)
            print time.replace('AM','').replace(match.group(1),new_x)
            
        elif match.group(2) == 'PM':
            x = int(match.group(1))
            if x == 12:
                new_x = '12'
            else:
                new_x = str(x+12)
            print time.replace('PM','').replace(match.group(1),new_x)
    