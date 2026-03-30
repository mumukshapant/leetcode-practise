class Solution(object):
    def calculate(self, s):
        """
        Evaluate expression string s
        """

        stack = []  # stores intermediate results
        num = 0     # current number being built
        prev_op = '+'  # previous operator

        # Iterate through string
        for i in range(len(s)):
            char = s[i]

            # STEP 1: Build number if digit
            if char.isdigit():
                num = num * 10 + int(char)  # handle multi-digit numbers

            # STEP 2: If operator OR end of string → process previous number
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:

                # STEP 3: Process based on previous operator

                if prev_op == '+':
                    # Push number as is
                    stack.append(num)

                elif prev_op == '-':
                    # Push negative number
                    stack.append(-num)

                elif prev_op == '*':
                    # Multiply with last element (higher precedence)
                    last = stack.pop()
                    stack.append(last * num)

                elif prev_op == '/':
                    # Divide with last element (truncate toward zero)
                    last = stack.pop()
                    # Python division floors for negatives, so fix it
                    stack.append(int(last / float(num)))

                # Update operator for next iteration
                prev_op = char

                # Reset current number
                num = 0

        # STEP 4: Final result is sum of stack
        return sum(stack)