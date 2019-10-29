class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        
        创建一个可以滑动的窗口[]，每当下一个元素j在集合里面不存在，
        则向右滑动一格，同时将窗口的size和原来进行比较。这个行为
        相当于向右拓展窗口的大小。
        当遇到重复的元素，则将数组最左侧的元素从集合中删除，并且左
        移左侧窗口。
        """
        


        result = 0
        hs = set()
        i = j = 0
        while i < len(s) and j < len(s):
            if s[j] not in hs:
                hs.add(s[j])
                result = max(result, j-i+1)
                j += 1
            else:
                hs.remove(s[i])
                i += 1
        return result