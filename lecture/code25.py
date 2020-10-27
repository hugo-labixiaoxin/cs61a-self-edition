def bigs(t):
    def f(a,x):  #x is the max_ancestor
        if a.label>x:
            return 1+sum([f(b,a.label) for b in a.branches])
        else:
            return sum([f(b,x) for b in a.branches])
    return f(t,t.label-1)

def smalls(t):
    result=[]
    def process(t):
        if t.is_leaf():
            return t.label 
        else:
            smallest=min([process(b) for b in t.branches ])
            if t.label<smallest:
                result.append(t.label)
            return  min(smallest,t.label)
    process(t)
    return result
class Tree:
    def __init__(self,label,branches=[]):
        self.label=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches=list(branches)
    def __repr__(self):
        if self.branches:
            branch_str=', '+repr(self.branches)
        else:
            branch_str=''
        return 'Tree({0}{1})'.format(repr(self.label),branch_str)
    def __str__(self):
        return '\n'.join(self.indented())
    def indented(self):
        lines=[]
        for b in self.branches:
            for line in b.branches:
                lines.append('  '+line)
        return [str(self.label)]+lines
    def is_leaf(self):
        return not self.branches