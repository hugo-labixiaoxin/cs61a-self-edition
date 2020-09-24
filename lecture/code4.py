def make_adder(n):
    def adder(k):
        return k*k+n
    return adder