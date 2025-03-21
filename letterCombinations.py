import time, math
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pass
            


            


if __name__ == '__main__':
    #test1
    start_time = time.perf_counter()
    digits = "23"
    assert Solution.letterCombinations(digits) == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )

    #test2
    start_time = time.perf_counter()
    piles = [30,11,23,4,20]
    h =5
    assert Solution.minEatingSpeed(piles,h) in {30 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )