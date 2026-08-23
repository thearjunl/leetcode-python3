class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2

        left = num[:half]
        right = num[half:]

        left_sum = sum(int(ch) for ch in left if ch != "?")
        right_sum = sum(int(ch) for ch in right if ch != "?")

        left_questions = left.count("?")
        right_questions = right.count("?")

        # An odd number of '?' gives Alice the winning move.
        if (left_questions + right_questions) % 2 == 1:
            return True

        # Bob can force equality only in this exact case.
        return left_sum - right_sum != 9 * (right_questions - left_questions) // 2