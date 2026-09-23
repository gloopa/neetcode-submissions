class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        #Time Complexity would be O(n logn) since it used quicksort?
        