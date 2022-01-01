class Solution:
    def Anagrams(self, words, n):
       temp={}
       result=[]
       for p in words:
           q=sorted(p)
           quer=''.join(q)
           if quer in temp.keys():
               temp[quer]+='0'+p
           else:
               temp[quer]=p
       
       for p in temp.values():
           result.append(p.split('0'))
       
       return result



if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

