class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0 
        duplicates = set() 

        for right in range(len(s)):
            
            while s[right] in duplicates: 
                duplicates.remove(s[left])
                left+=1 
            duplicates.add(s[right])
            length = max(length, len(duplicates))
        
        return length

        