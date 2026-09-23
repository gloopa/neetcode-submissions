class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if self.isPalindrome(s):
            return True 
        else:
            for i in range(len(s)):
                if self.isPalindrome(s[:i] + s[i+1:]):
                    return True
                
        return False
      
            
    



    def isPalindrome(self, s):
        string = ''.join(char.lower() for char in s if char.isalnum())
        return string == string[::-1]


        