# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                if not self.isRepeat(nums, first, i):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return res

    def isRepeat(self, nums, first, n):
        temp = nums[n]
        for i in range(first, n):
            if nums[i] == temp:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
