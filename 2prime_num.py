start,end=input().split()
start=int(start)+1
end=int(end)
for num in range(start,end):
    for x in range(2,num):
        if(num% x == 0):
            break
    else:
        print(num, end=" ")
