# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# My solution works on the Leetcode page. Accepted.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n-1

        while left < right:
            mid = (left+right)//2   # integer division, rounds down
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        # left is now >= right... or only =
        if isBadVersion(left):
            return left
        else:
            return left + 1
