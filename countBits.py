class Solution:
    def countBits( n: int) -> list[int]:
        """
        Algo:
        if a number is even, its binary has same number of bits as its half. 
        integer division shifts the binary to the right by 1 . The rightmost bit in even number is 0. So the number of bits set to 1 in an even number remains same when we divide it by 2. dp[i] = dp[i//2]
        If the number is odd, the rightmost bit is 1. if we look at the even number preceeding this number, the number of set bits in it will be 1 less than the odd number. so dp[i] = dp[(i-1)//2] +1 

        """
        dp = [0]*(n+1) #list to keep count of 1's in binary representation
        for i in range(1,n+1):
            if i%2==0: # even number
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[(i-1)//2] + 1
        print(dp)
        return dp
assert Solution.countBits(5) == [0,1,1,2,1,2]
        