class Link:
    empty=()
    def __init__(self,first,rest=empty):
        self.first=first
        self.rest=rest
    def __getitem__(self,i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]
    def  __len__(self):
        return 1+len(self.rest)
    def __repr__(self):
        if self.rest:
            rest_str=', '+repr(self.rest)
        else:
            rest_str=''
        return 'Link({0}{1})'.format(self.first,rest_str)
def add(s,v):
    assert s is not List.empty
    if s.first>v:
        s.first,s.rest=v,Limk(s.first,s.rest)
    elif s.first<v and empty(s.rest):
        s.rest=Link(v)
    elif s.first<v:
        add(self.rest,v)
    return s