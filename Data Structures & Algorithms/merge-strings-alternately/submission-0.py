class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        string = ''
        if len(word1) < len(word2):
            while left < len(word1):
                string += word1[left] 
                string += word2[left]
                left+=1 
            string += word2[left:] 
        if len(word1) >= len(word2):
            while left < len(word2):
                string += word1[left]
                string += word2[left]
                left+=1
            string += word1[left:] 
 
        return string

    
    
            



        