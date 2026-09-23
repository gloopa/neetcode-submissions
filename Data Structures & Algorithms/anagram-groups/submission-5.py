class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can sort every string in strings list. Then if they equal each other return 
        #o(n^2) :(((
        #hashmap -> have sorted strings -> if its not in hashmap -> empty else, add to value of dict retirnl list 

        hashmap = {}
        for string in strs: #O(N)
            sorted_string = ''.join(sorted(string)) #O(n logn)
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(string) 
        return list(hashmap.values()) #time complexity = 
        