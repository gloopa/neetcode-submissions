class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate = set()
        length = 0 
        left = 0
        for right in range(len(s)):
            while s[right] in duplicate: 
                duplicate.remove(s[left])  
                left+=1 
            duplicate.add(s[right])
            length = max(length, len(duplicate))
        return length


        