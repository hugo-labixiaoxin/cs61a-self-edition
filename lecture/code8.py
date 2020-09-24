def trace1(f):
    def traced(x):
        print('calling',f,'on argument',x)
        return f(x)
    return traced
@trace1
def square(x):
    return x*x
@trace1
def sum_square(n):
    total,k=0,1
    while k<=n:
        total,k=total+square(k),k+1
    return total
