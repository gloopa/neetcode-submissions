class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        positions = [0] * 26 

        for i in range(len(s)):
            positions[ord(s[i]) - ord('a')] += 1 
            positions[ord(t[i]) - ord('a')] -= 1 
        
        for val in positions:
            if val != 0:
                return False
        return True
