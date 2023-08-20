class Solution:
    # Time Complexity O(n)
    # Space Complexity O(1)
    def isPalindrome2(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
                    continue
            left += not s[left].isalnum()
            right -= not s[right].isalnum()
        return True
    
    # Time Complexity O(n)
    # Space Complexity O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s.lower() if i.isalnum()])
        return s == s[::-1]
