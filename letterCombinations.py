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
        
        choices = [ y for x in digits for  y in digitMap[x] ]
        state = []
        combinations = []
        
        def is_valid_choice(choice, state):
            #two pairs
            if len(state)== 0:
                return True # first choice is free
            index = 0
            for letter in state:
                if letter not in digitMap[digits[index]]:
                    return False
                index+=1
            #now check choice is from the next available digitmap
            if choice not in digitMap[digits[index]]:
                return False
            return True


        def make_choice(choice, state):
            state.append(choice)
        def undo_choice(choice, state):
            state.pop()
        def is_solution(state, combinations): 
            if len(state)== len(digits) and ''.join(state[:]) not in combinations:
                return True
            return False
        def backtrack(state, choices, combinations):
            if is_solution(state, combinations):
                combinations.append(''.join(state[:]))
                print('combination got a new succss state', combinations)
                return # this is the base case that stops the recursion
            #is solution doesn't allow for duplicates, so if we have reached the intended string length, we need to return without adding to combinations
            if len(state) == len(digits):
                return
            for choice in choices:
                if is_valid_choice(choice, state):
                    make_choice(choice, state)
                    backtrack(state, choices, combinations)
                    undo_choice(choice, state)
        backtrack(state, choices, combinations)
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