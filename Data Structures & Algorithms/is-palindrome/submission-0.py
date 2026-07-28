class Solution:
    def isPalindrome(self, s: str) -> bool:
        pallindrome = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].lower().isalnum():
                pallindrome += s[i].lower()
        if pallindrome == pallindrome[::-1]:
            return True
        return False