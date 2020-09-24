def fib(n):
    pred,curr=0,1
    k=0
    while k<n:
        pred,curr=curr,pred+curr
        k=k+1
    return curr
