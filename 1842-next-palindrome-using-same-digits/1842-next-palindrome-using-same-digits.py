class Solution(object):
    def nextPalindrome(self, num):
        """
        :type num: str
        :rtype: str
        """

        # Total length of the palindrome
        n = len(num)
        left_half = list(num[:n // 2])

        def next_permutation(arr):
            """
            Make arr into the next bigger arrangement.

            Returns True if possible.
            Returns False if arr is already the biggest arrangement.
            """

            # STEP 1:
            # Move from right to left and find the first place
            # where the digits are increasing.
            #
            # Why?
            # This is the first place where we can make the number bigger.
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1

            # If no such position exists, arr is already the biggest
            if i < 0:
                return False

            # STEP 2:
            # Find the smallest digit on the right side that is bigger than arr[i]
            #
            # Why?
            # We want the next bigger arrangement, so increase by the smallest amount.
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1

            # Swap them
            arr[i], arr[j] = arr[j], arr[i]

            # STEP 3:
            # Reverse the part after i
            #
            # Why?
            # After making the number bigger, we want the remaining part
            # to be as small as possible.
            left = i + 1
            right = len(arr) - 1

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            return True

        # Try to make the left half bigger
        if not next_permutation(left_half):
            return ""

        # Turn updated left half back into string
        left_part = "".join(left_half)

        # If length is even:
        # full palindrome = left + reverse(left)
        if n % 2 == 0:
            return left_part + left_part[::-1]

        # If length is odd:
        # keep middle digit unchanged
        middle_digit = num[n // 2]
        return left_part + middle_digit + left_part[::-1]