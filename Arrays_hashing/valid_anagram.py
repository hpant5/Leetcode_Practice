# Given two strings return true if they are anagrams of each other and false if not
# Anagrams have the same characters but the order may be different 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorted the lists and then compared if they are the same or not
        s = sorted(s)
        t = sorted(t)
        if s==t:
            return True
        else:
            return False