t=int(input())
for i in range(t):
    n,key=list(map(int,input().split()))
    array=list(map(int,input().split()))
    temp = 0
    count = 0
    result=1
    for j in range(n):
        for k in range(temp,n):
            result*=array[k]
            if result>=key:
                result/=array[k]
                break
        else:
            k=n
        count+=(k-j)
        result=(result/(array[j]))
        temp=k
        if k-j==0:
            result=1
            temp=k+1
    print(count)