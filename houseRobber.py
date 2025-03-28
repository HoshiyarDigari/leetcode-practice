class Solution:
    def rob(nums: list[int]) -> int:
        """
        f(i) = max (f(i-2) to f(0)) + list(i)
        the DAG shows we can get to i from all other nodes except i-1
        """
        if len(nums)==1:
            return nums[0]
        loot_money = [0] * len(nums)
        loot_money[0], loot_money[1] = nums[0], nums[1]
        print(loot_money)

        for i in range(2, len(nums)):
            loot_money[i] = nums[i] + max(loot_money[:i-1])
            print(loot_money)
        return max(loot_money)
#test1
assert Solution.rob([1,2,3,1])==4