st1,st2=input().split()
a=int(st1)
b=int(st2)
for i in range(a+1,b):
  c=0
  for j in range(1,b):
    if(i%j==0):
      c=c+1
    if(c==2):
      print(i, end=" ")
