class Solution:
    def singleNumber( nums: list[int]) -> int:
        """
        Algo:
        We use XOR bit operator. 
        XOR with itself is 0. XOR with 0 is itself.
        XOR is associative that is order doesn't matter in XOR of many number.
        we xor all inputs and all duplicates cancel themselves out leaving the single number.
        """
        result = 0
        for num in nums:
            result^=num
        return result
    



assert Solution.singleNumber([4,1,2,1,2])==4