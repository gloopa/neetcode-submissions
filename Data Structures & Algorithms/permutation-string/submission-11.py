class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        char1 = [0] * 26
        char2 = [0] * 26
        for char in s1:
            char1[ord(char) - ord('a')] +=1 

        for right in range(len(s2)):
            char2[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                char2[ord(s2[left]) - ord('a')] -= 1 
                left+=1 
            
            if right - left + 1 == len(s1) and char1 == char2:
                return True
        
        return False

        