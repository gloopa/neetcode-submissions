class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate = set()
        left = 0
        length = 0
        for char in range(len(s)):
            while s[char] in duplicate: 
                duplicate.remove(s[left])
                left+=1
            duplicate.add(s[char])
            length = max(length, len(duplicate))
        return length 


        #"zxyzxyz"    
        