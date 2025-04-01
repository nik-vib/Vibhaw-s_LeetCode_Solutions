class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] represents max points from questions[i:]

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            skip = dp[i + 1]  # Points from skipping current question
            solve = points + dp[min(n, i + brainpower + 1)]  # Points from solving
            dp[i] = max(skip, solve)

        return dp[0]
