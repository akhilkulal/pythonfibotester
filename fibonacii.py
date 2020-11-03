def fibo1(n):
    #cannot handle datatypes and negative numbers
    if n == 0:
        return None
    elif n == 1:
        return '0'
    else:
        l = [0,1]
        x ,y = 0,1
        for i in range(2, n):
            z = x + y
            l.append(z)
            x = y
            y = z
    return l

def fibo2(n):
    #can't handle other datatypes
    if n < 0:
        return None
    return fibo1(n)

def fibo3(n):
    #can't handle other datatypes and zero case
    if n == 1:
        return '0'
    else:
        l = [0,1]
        x ,y = 0,1
        for i in range(2, n):
            z = x + y
            l.append(z)
            x = y
            y = z
    return l




    