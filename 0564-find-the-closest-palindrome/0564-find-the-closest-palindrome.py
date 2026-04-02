class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        # Convert original string into integer so we can compare distances easily
        original_number = int(n)

        # Length of the number string
        length = len(n)

        def build_palindrome(first_part, is_even_length):
            """
            Build a palindrome from the left side.

            Why this helper?
            - A palindrome is made by mirroring one side onto the other.
            - So if we know the left side, we can construct the whole number.

            Example:
            first_part = 12, even length
            -> 1221

            first_part = 12, odd length
            -> 121
            """

            # Convert first part into string so we can reverse it
            first_part_str = str(first_part)

            # If total length should be even:
            # mirror the full left part
            if is_even_length:
                return int(first_part_str + first_part_str[::-1])

            # If total length should be odd:
            # do NOT repeat the middle digit
            # Example: 12 -> 121, not 1221
            return int(first_part_str + first_part_str[:-1][::-1])

        # We take the first half of the number.
        # Why?
        # Because in a palindrome, once the left side is fixed,
        # the right side is just its mirror.
        #
        # For odd length, we include the middle digit in this first part.
        # Example:
        # "123"  -> first part = "12"
        # "1234" -> first part = "12"
        first_part = int(n[:(length + 1) // 2])

        # Store all possible nearest palindrome candidates
        candidates = set()

        # Try building palindrome from:
        # 1) same first part
        # 2) one smaller
        # 3) one bigger
        #
        # Why?
        # Because the closest palindrome usually comes from
        # keeping the left/middle same or changing it slightly.
        for new_first_part in [first_part - 1, first_part, first_part + 1]:
            candidates.add(build_palindrome(new_first_part, length % 2 == 0))

        # Special edge case:
        # Number made of all 9s with one fewer digit
        #
        # Examples:
        # 10   -> 9
        # 100  -> 99
        # 1000 -> 999
        candidates.add(10 ** (length - 1) - 1)

        # Special edge case:
        # 1 followed by zeros and ending with 1
        #
        # Examples:
        # 9   -> 11
        # 99  -> 101
        # 999 -> 1001
        candidates.add(10 ** length + 1)

        # Remove the original number itself if it got generated
        # because answer is not allowed to be the same number
        if original_number in candidates:
            candidates.remove(original_number)

        # This will store the best answer found so far
        best_candidate = None

        # Check all candidates and choose the nearest one
        for candidate in candidates:

            # If this is the first candidate, take it for now
            if best_candidate is None:
                best_candidate = candidate
                continue

            # Distance of current candidate from original number
            current_difference = abs(candidate - original_number)

            # Distance of best candidate from original number
            best_difference = abs(best_candidate - original_number)

            # If current candidate is closer, update answer
            if current_difference < best_difference:
                best_candidate = candidate

            # If both are equally close, choose the smaller one
            elif current_difference == best_difference and candidate < best_candidate:
                best_candidate = candidate

        # Return answer as string because input/output format uses strings
        return str(best_candidate)