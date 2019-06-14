m,n=map(int, input().split())
for i in range(m, n):
   r = len(str(i))
   sum = 0
   temp = i
   while temp > 0:
       digit = temp % 10
       sum += digit ** r
       temp //= 10
   if i == sum:
       print(i,end=' ')
