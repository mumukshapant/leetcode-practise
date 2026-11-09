class Solution(object):
    def carPooling(self, nums, capacity):
        nums.sort(key=lambda x: x[1])

        prev = nums[0]
        active = [prev]
        currcap = prev[0]

        if currcap > capacity:
            return False

        for i in range(1, len(nums)):
            curr = nums[i]

            # Remove trips that have ended
            active = [trip for trip in active if trip[2] > curr[1]]

            currcap = sum(trip[0] for trip in active)

            # Add current trip
            currcap += curr[0]

            if currcap > capacity:
                return False

            active.append(curr)
            prev = curr

        return True