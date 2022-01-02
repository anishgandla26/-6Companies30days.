


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            len1 = len(str1)
            len2 = len(str2)
            
            def gcd(a,b):
                return b if a == 0 else gcd(b%a,a)
            gcd_res = gcd(len1, len2)
            
            prefix = str1[:gcd_res]
            prefix_len = gcd_res
            
            mult1 = len1//prefix_len
            mult2 = len2//prefix_len
            
            if prefix*mult1 == str1 and prefix*mult2 == str2:
                return prefix
            else:
                return ""

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        string1=input()
        string2=input()
        ob = Solution()
        ans = ob.gcdOfStrings(string1,string2)