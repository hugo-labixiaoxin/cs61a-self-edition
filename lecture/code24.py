def pi_4(n):
    y=0
    g=-1
    for i in range(n):
        g=-g
        y+=g/(2*i-1)
    return y
def memo(f):
    cache={}
    def memoized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    return memoized
        
    