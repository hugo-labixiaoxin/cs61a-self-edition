def end(n,d):
    while n>0:
        n,last=n//10,n%10
        print(last)
        if d==last:
            return None