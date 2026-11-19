from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = 0
        r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove an index that has left the window.
            if q[0] < l:
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res