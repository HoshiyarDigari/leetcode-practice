class Solution:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        """
        Algo:
        m = len(text1) n = len(text2)
        we create a matrix dp of dimensions (m+1)x(n+1)
        this matrix holds the length of the longest common subsequence. dp[i][j] is the LCS of strings text1[:i] and text2[:j]
        if text1[i-1] matches text2[j-1] then dp[i][j] = dp[i-1][j-1] + 1
        if they dont match, then dp[i][j] is max[dp[i-1][j], dp[i][j-1]]
        return dp[m][n]
        """
        if not text1 or not text2:
            return 0 # if any of the string is empty then we have no common subsequence
        m,n = len(text1), len(text2)
        
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # fill the rest of the dp 
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]== text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        print(dp, dp[m][n])
        return dp[m][n]


assert Solution.longestCommonSubsequence("abcde","ace") == 3