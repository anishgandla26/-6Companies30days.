

def encode(arr):
    i = 0
    ans = ""
    
    while i < len(arr):
        temp = arr[i]
        cnt = 1
        while i + 1 < len(arr) and temp == arr[i + 1]:
            i += 1
            cnt += 1
        ans += temp + str(cnt)
        i += 1
    return ans
    


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
