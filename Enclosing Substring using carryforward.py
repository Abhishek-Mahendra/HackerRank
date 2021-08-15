def check(ca,cb):
    i='a'
    while(i<='z'):
        if ca[i]>=cb[i]:
            x=1
        else:
            return False
        i=chr(ord(i)+1)
    return True
    
def findMinLen(b,a):
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

    ans=9999999999
    
    for i in range(len(a)):
        for j in range(i,len(a)):
            ca[a[j]]+=1
            if (check(ca,cb)==True):
                ans=min(ans,j-i+1)
        x='a'
        while(x<='z'):
            ca[x]=0
            x=chr(ord(x)+1)
    return ans if ans!=9999999999 else -1
for _ in range(int(input())):
    val,txt=map(str,input().split())
    print(findMinLen(val,txt))
