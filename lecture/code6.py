def search(f):
    x=0
    while True:
        if f(x):
            return x
        x=x+1
def square(x):
    return x*x
def inverse(f):
    return lambda y: search(lambda x: f(x)==y)