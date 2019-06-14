m,n=map(int, input().split())
for mr in range(m+1,n):
   if mr > 1:
       for i in range(2,mr):
           if (mr % i) == 0:
               break
       else:
           print(mr,end=' ')
