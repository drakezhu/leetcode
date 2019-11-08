class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        先从左上角用BFS将最小值填完；
        再从右下角往上走一遍
        '''
        r, c = len(matrix), len(matrix[0])
        dp = [[20000] * (c + 2) for i in range(r + 2)]
        for i in xrange(1, r + 1):
            for j in xrange(1, c + 1):
                if matrix[i - 1][j - 1] == 0:
                    dp[i][j] = 0
                else:
                    if i >= 1 and j >= 1:
                        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i][j])
        
        for i in reversed(xrange(1, r + 1)):
            for j in reversed(xrange(1, c + 1)):
                if matrix[i - 1][j - 1] == 0:
                    dp[i][j] = 0
                else:
                    if i >= 1 and j >= 1:
                        dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j])
                        
        dp = [dp[i][1:c + 1] for i in range(1, r + 1)]
        return dp