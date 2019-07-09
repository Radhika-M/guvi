s=input()
c=0
for i in range(0,len(s)):
    if(s[i].isdigit() or s[i].isalpha() or s[i]==' '):
        continue
    else:
        c=c+1
print(c)
