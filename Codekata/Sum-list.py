N,K=map(int,input().split())
lis=list(map(int,input().split()))
sum=0
for i in range(0,K):
    sum=sum+lis[i]
print(sum)
