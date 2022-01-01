def overlap(L1x,L1y,R1x,R1y,L2x,L2y,R2x,R2y):

    if(L1x>R2x or L2x>R1x):
        return 0

    if(L1y <= R2y or L2y <=R1y):
        return 0
    if(L1x==R2x or L2x==R1x):
        return 1


    return 1




t=int(input())
for i in range(t):

    l1x,l1y,r1x,r1y=map(int,input().split())
    l2x,l2y,r2x,r2y=map(int,input().split())

    print(overlap(l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y))