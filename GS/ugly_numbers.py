from bisect import insort
a = [1,2,3,4,5]
x = 0
j = 1
f = dict()
f = {1:0,2:0,3:0,4:0,5:0}
while(x!=10**4):
  if(a[j] * 2 not in f):
    insort(a, a[j]*2)
    f[a[j] * 2] = 0
  if(a[j] * 3 not in f):
    insort(a, a[j]*3)
    f[a[j] * 3] = 0
  if(a[j] * 5 not in f):
    insort(a, a[j]*5)
    f[a[j] * 5] = 0
  j = j+1
  x = x+1
for _ in range(int(input())):
  num = int(input())
  print(a[num-1])