# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        # 动态规划：时间复杂度O(n),空间复杂度O(n)

        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            t = int(s[i - 1])
            if t >= 1 and t <= 9:
                dp[i] += dp[i - 1]  # 最后一个数字解密成一个字母
            if i >= 2:  # 下面这种情况至少要有两个字符
                t = int(s[i - 2]) * 10 + int(s[i - 1])
                if t >= 10 and t <= 26:
                    dp[i] += dp[i - 2]  # 最后两个数字解密成一个一个字母
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
