def check(ca,cb):
    i='a'
    while(i<='z'):
        if ca[i]>=cb[i]:
            x=1
        else:
            return False
        i=chr(ord(i)+1)
    return True

def findMinLen(b,a,l):
    ca={}
    cb={}
    reset={}
    i='a'
    while(i<='z'):
        reset[i]=0
        ca[i]=0
        cb[i]=0
        i=chr(ord(i)+1)
    for i in b:
        cb[i]+=1
    for i in range(l):
        ca[a[i]]+=1
    if check(ca,cb):
        return True
    for i in range(1,len(a)-l+1):
        ca[a[i-1]]+=-1
        ca[a[i+l-1]]+=1
        if check(ca,cb)==True:
            return True
    return False
        
        
def binarysearch(a,b):
    low=len(b)
    high=len(a)
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(findMinLen(b,a,mid)==True):
            ans=mid
            high=mid-1
        else:
            low=mid+1
            
    return ans 
    
for _ in range(int(input())):
    b,a=map(str,input().split())
    print(binarysearch(a,b))
