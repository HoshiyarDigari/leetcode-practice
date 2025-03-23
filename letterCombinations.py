import time, math
class Solution:
    def letterCombinations(digits: str) -> list[str]:
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
        if not digits:
            return []
        digitMap = {'2':('a', 'b', 'c'), '3':('d','e','f'), '4':('g','h','i'), '5':('j','k','l'), '6':('m','n','o'), '7':('p', 'q','r','s'), '8':('t','u','v'), '9':('w', 'x','y','z')}
        
        def backtrack(state, combinations, index):
            #if index exceeds the digits array, we have reached the depth of the tree and need to back track, this is the step that stops the recursion
            if index== len(digits):
                combinations.append(''.join(state))
                return
            choices = [ x for x in digitMap[digits[index]]]
            for choice in choices:
                state.append(choice) #make choice
                backtrack(state, combinations, index + 1)
                #undo choice - backtrack
                state.pop()
                
    
        index = 0
        state = []
        combinations = []
        backtrack(state,combinations, index)
        print(combinations)
        return combinations


            


            


if __name__ == '__main__':
    #test1
    start_time = time.perf_counter()
    digits = "22"
    assert Solution.letterCombinations(digits) == ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]
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