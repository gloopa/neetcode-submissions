class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        valid = set() 
        length = 0 

        for right in range(len(s)):
            while s[right] in valid:
                valid.remove(s[left])
                left+=1 
            valid.add(s[right])
            length = max(length, (right-left+1))
        
        return length
            

        