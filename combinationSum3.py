import time, math
class Solution:
    def combinationSum3( k: int, n: int) -> list[list[int]]:
        """
        Algo:
        we will use the general backtracking template as below
        def backtrack(choices, state, constraints, solution):
            if is_solution(state, solution):
                if len(state)==len(digits):
                    return True
                return False
            for choice in choices:
                if is_valid(choice, state):
                    make_choice(choice, state)
                    backtrack(choices, state, constraints, solution)
                    undo_choice(choice,state)
        defining is_valid choice is the main bulk of the algorithm
        """
        
        def backtrack(numbers_selected,current_sum, combinations, position):

            #if position exceeds k , we have to stop recursion
            if position>k:
                return
            #if we have reached the requird sum, we add the numbers to combinations
            
            choices = [ x for x in range(1,10)]
            for choice in choices:
                #check if this choice is valid as per constraints, we are not allowed to repeat the number
                if choice not in numbers_selected:

                    numbers_selected.append(choice) #make choice
                    current_sum+=choice
                    if current_sum == n:
                        combinations.append(numbers_selected[:])
                    backtrack(numbers_selected,current_sum, combinations, position + 1)
                    #undo choice - backtrack
                    current_sum-=numbers_selected.pop()
                    
                
    
        position = 1 #this will track each digit for the k numbers
        numbers_selected = []
        combinations = []
        current_sum = 0
        backtrack(numbers_selected,current_sum, combinations, position)
        print(combinations)
        return combinations


            


            


if __name__ == '__main__':
    #test1
    start_time = time.perf_counter()
    k ,n = 3, 7
    assert Solution.combinationSum3(k,n) == [[1,2,4]]
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )

    #test1
    start_time = time.perf_counter()
    digits = ""
    assert Solution.letterCombinations(digits) == []
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )

    #test1
    start_time = time.perf_counter()
    digits = "2"
    assert Solution.letterCombinations(digits) == ["a","b","c"]
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )