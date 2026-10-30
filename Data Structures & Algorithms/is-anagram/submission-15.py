class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False

        pos = [0] *26 

        for i, char in enumerate(s):
            pos[ord(char) - ord('a')] += 1
            pos[ord(t[i]) - ord('a')] -= 1 
        
        for num in pos:
            if num != 0:
                return False 
        
        return True
        