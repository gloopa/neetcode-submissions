class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # fixed list of size 26 (# of letters in alphabet) -> ascii of current char - ascii of a => position ()
        # time: O(N) linear, space: O(1) fixed 

        # alternative -> 2 frequency hashmaps for each then check if they are equal 

        # Counter(s) == Counter(t) , O(N)

        charpos = [0] * 26 
        if len(s) != len(t):
            return False

        for i, char in enumerate(s):
            charpos[ord(char) - ord('a')] += 1 
            charpos[ord(t[i]) - ord('a')] -= 1 
        
        for freq in charpos:
            if freq != 0:
                return False 
        
        return True
