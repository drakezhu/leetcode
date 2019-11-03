class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        '''
        创建一个m*n的表格，遍历两个字符串
        如果 对应位置相等（s1[i] = s2[j]）
        则将当前位置赋值为对角线的位置的值+1
        如若不等，则在两个长度-1的子字符串中
        寻找大的那个
        '''
        i = j = 0
        m = len(text1)+1
        n = len(text2)+1
        l = [[0 for i in range(m)] for j in range(n)] 
        
        i = j = 0
        while i < m-1:
            j = 0
            while j < n-1:
                #print text1[i]
                #print text2[j]
                if text1[i] == text2[j]:
                    l[j+1][i+1] = 1 + l[j][i]
                else:
                    l[j+1][i+1] = max(l[j+1][i],l[j][i+1])
                j += 1
                #print l
                #print l[1][2]
            i += 1
        return l[n-1][m-1]

                    