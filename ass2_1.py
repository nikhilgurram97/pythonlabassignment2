str=input("enter the required sentence to be purified")
wlist=str.split()
wdict={}
count=0
for word in wlist:
    if word in wdict:
        wdict[word]+=1
    else:
        wdict[word]=1
nlist=list(wdict.keys())
nlist.sort()
str1 = ' '.join(nlist)
print(str1)