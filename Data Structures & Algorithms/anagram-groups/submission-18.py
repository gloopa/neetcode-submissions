class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for string in strs:
            pos = [0] * 26 
            for char in string:
                pos[ord(char) - ord('a')] += 1 
            hashmap[tuple(pos)].append(string)
        
        return list(hashmap.values())
            
        