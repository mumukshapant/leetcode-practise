class Solution(object):
    def search(self, nums, t):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == t:
                return mid

            # Left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= t < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < t <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1