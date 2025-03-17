# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pick=7
    if num == pick:
        return 0
    if num < pick:
        return 1
    return -1

class Solution:
    def guessNumber( n: int) -> int:
        """
        Algo:
        implement basic binary search from 1 to n
        """
        if guess(n)== 0:
            return n
        start, end = 1,n
        while(True):
            my_guess = (start + end)//2
            result = guess(my_guess)
            if result == 0:
                return my_guess 
            elif result == 1: #guessed too low so bring up the start point
                start = my_guess + 1 # important to set one more than guess to avoid infinite loops and better runtimes, same with end
            else:
                end = my_guess -1 


assert Solution.guessNumber(10)== 6




