s,w=map(int ,input().split())
s=s^w
w=s^w
s=s^w
print(s,w)
