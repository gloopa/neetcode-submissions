class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1) sorted string -> words  O(m log n) time, O(n) space
        # 2) fixed length list of 26 containing frequency of letters -> words O(m * n) time, O(n) space 

        anagrams = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1 
            anagrams[tuple(freq)].append(string)
        
        return list(anagrams.values())
        


        