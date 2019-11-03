class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        异或运算符和交换律，可以将所有数字异或，
        则最后剩下的结果为0异或a，此处a为唯一
        的single number
        """
        a = 0
        for i in nums:
            a ^= i
        return a