# Enter your code here. Read input from STDIN. Print output to STDOUT
def compareBits(a, b, x):
    c = 0
    i = 0
    while i < len(a):
        c+= 1 if int(a[i]) != int(b[i]) else  0
        i+=1
    if c == x:
        return 1
    else:
        return 0

def compare(l, x):
    z = 0
    ls = [bin(k).replace("b","0") for k in l]
    i = 0
    while i < len(ls):
        j = 0
        while j < len(ls):
            if i < j and int(ls[i])^int(ls[j]):
                z += compareBits(ls[i], ls[j], x)
            j += 1
        i+=1
    return z
                
l=[]
n,x = [int(x) for x in input().split()] 

l = [int(x) for x in input().split() if len(l) <= n]
  
res = compare(l, x)
print(res)