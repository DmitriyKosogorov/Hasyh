def my_hash(key, n):
    return hash(key)%(2**n)

def my_hash1(key,n):
    p=19476320
    x=2534512
    code=0
    for i in range(len(key)):
       code=code+ord(key[i])*(x**i)
    code=code%p
    code1=str(code)
    if(len(code1)>(n/4)):
        code1=code1[:(n/4)]
    if(len(code1)<(n/4)):
        while(len(code1)<(n/4)):
            code1=code1+'0'
    return(code1)

def my_hash2(key,n):
    code=0
    fin_code="00000000"
    for i in range(len(key)):
        code=ord(key[i])
        s=""
        while(code>0):
            s=str(code%2)+s
            code=int(code/2)
        for j in range(len(s)):
            fin_code[j]=str(int(fin_code[j])+int(s[j]))
    print(fin_code)
    return fin_code
    

file=open("endict.txt","r")
kollizies={}
lines=file.readlines()
for line in lines:
    #s=my_hash(line,32)
    s=my_hash2(line,32)
    #print(s)
    if s in kollizies:
        kollizies[s]=kollizies[s]+1
    else:
        kollizies[s]=1
summa=0
for i in kollizies:
    if kollizies[i]>1:
        summa=summa+kollizies[i]-1
print(summa)