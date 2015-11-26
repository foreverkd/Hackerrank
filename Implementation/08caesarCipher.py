def caesarCipher():
    n = int(raw_input())
    s = raw_input()
    k = int(raw_input())
    data = []
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            data.append(chr((ord(i) - ord('a') +k)%26 +ord('a')))
        elif ord('A') <= ord(i) <= ord('Z'):
            data.append(chr((ord(i) - ord('A') + k) %26 +ord('A')))
        else:
            data.append(i)
            
    output = ''.join(data)
    print output, data
            
            