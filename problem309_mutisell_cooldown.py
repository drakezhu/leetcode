class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p_has_stock, p_cooldown, p_canbuy = -float("inf"), 0, 0
        for price in prices:
		    # update the profit for each day
            p_has_stock, p_cooldown, p_canbuy = max(p_has_stock, p_canbuy - price), p_has_stock + price, max(p_cooldown, p_canbuy)
            print "prices: " + str(price) + " stack: " + str(p_has_stock) + " cool: " + str(p_cooldown) + " can: " + str(p_canbuy)
        return max(p_cooldown, p_canbuy)

        '''
        p_has_stock = 持有一个股份情况下当前最高的利润
        p_cooldown = 把当前股票卖了的最高利润
        p_canbuy = 当前股票不卖，但没有股票的最高利润
        '''