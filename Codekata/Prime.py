m=int(input())
if m>1:
    for i in range(2,m):
      if(m%i)==0:
        print("no")
    else:
      print("yes")
else:
    print("no")
