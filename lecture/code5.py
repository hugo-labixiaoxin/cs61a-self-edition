def search(f):
    x=0
    while True:
        if f(x):
            return x
        x+=1
def inverse(f):
    def fun1(y):
        def fun2(x):
            return f(x)==y
        return search(fun2)
    return fun1
def square(x):
    return x*x
