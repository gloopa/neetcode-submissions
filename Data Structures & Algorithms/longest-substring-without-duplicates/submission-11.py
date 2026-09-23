class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in duplicates:
                duplicates.remove(s[left])
                left+=1 
            duplicates.add(s[right])
            length = max(length, right-left+1)
        return length
                    
