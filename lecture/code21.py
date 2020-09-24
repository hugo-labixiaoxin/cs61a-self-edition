def search(query,ranking=lambda r: -r.stars ):
    results=[r for r in Restaurant.all if query in r.name]
    return sorted(results,key=ranking)
def reviewed_both(r,s):
    return fast_overlap[r.reviewers,s.reviewers]
def fast_overlap(s,t):
    i,j,count=0,0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            count,i,j=count+1,i+1,j+1
        elif s[i]<t[j]:
            i+=1
        else:
            j+=1
    return count
class Restaurant:
    all=[]
    def __init__(self,name,stars,reviewers):
        self.name,self.stars=name,stars
        self.reviewers=reviewers
        Restaurant.all.append(self)
    def similar(self,k):
        "返回最相似的k所餐馆"
        others=Restaurant.all
        others.remove(self)
        sorted (others,key=lambda r :similarity(self,r))[:k]
    def __repr__(self):
        return '<'+self.name+'>'

    
results=search('Thai')
for r in results:
    print(r,'is similar to',r.similar(3))