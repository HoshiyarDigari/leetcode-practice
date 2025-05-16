class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Algo:
        we compare each bit place and decide if we need to flip and how many to flip
        """
        flip_count=0
        print(bin(a), bin(b), bin(c))
        length = max(c.bit_length(), a.bit_length(), b.bit_length())
        for i in range(length):
            if (c >> i) & 1: # bit is 1 in c
                if not ((b>>i)&1) and not((a>>i)&1): # both a and b have 0, we need to flip one of them
                    flip_count+=1
                    print(f'flipped {i}th bit, flip count={flip_count}')
            else:#bit is 0 in c,  bits need to be 0 in a and b
                if (a>>i)&1:
                    flip_count+=1
                    print(f'flipped {i}th bit, flip count={flip_count}')
                if (b>>i)&1:
                    flip_count+=1
                    print(f'flipped {i}th bit, flip count={flip_count}')
        
        return flip_count
    





answer = Solution()
# assert answer.minFlips(2,6,5)==3
# assert answer.minFlips(4,2,7)==1
assert answer.minFlips(10,9,1) == 3