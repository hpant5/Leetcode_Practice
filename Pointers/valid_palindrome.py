import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  re.sub(r'[^a-zA-Z0-9]', '', s)
        ch  = s[::-1]
        s = s.lower()
        ch  = ch.lower()
        if s==ch:
            return True
        else:
            return False

#simple approach substitute anything which is not alphanumberic, reverse the string and keep both lower and compare 