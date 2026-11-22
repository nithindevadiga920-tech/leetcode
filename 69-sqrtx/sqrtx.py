class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 1:
            x_new = int("1" + "0" * (len(str(x)) // 2))
            while True:
                nxt = 0.5 * (x_new + (x / x_new))
                if int(nxt) == int(x_new):  # Stops the moment it converges (~6 steps)
                    return int(nxt)
                x_new = nxt
        if x==1:
            return 1
        if x==0:
            return 0
