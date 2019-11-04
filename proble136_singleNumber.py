class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        异或一串相同的字符串，结果为0，一旦
        出现不相同的，则异或之后会变成那个值
        """
        a = 0
        for i in nums:
            a ^= i
        return a