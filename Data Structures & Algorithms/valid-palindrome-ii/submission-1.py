class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        for i, char in enumerate(s):
            newstr = s[:i] + s[i+1:]
            if self.palindrome(newstr):
                return True 
        
        return False





    def palindrome(self, string):
        newStr = ''
        for c in string:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1] 
    
