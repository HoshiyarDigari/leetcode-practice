
def removeStars( word):
    """
    :type word: str
    :rtype: str
    algo:'
    - scan word left to right
        if char is not * - add to list(stack)
        if char is * - remove last item from list
    - return the stack
    """
    stack = []
    [stack.append(char) if char!='*' else stack.pop() for char in word]
    # for char in word:
    #     if char != '*':
    #         stack.append(char)
    #     else:
    #         stack.pop()
    print(''.join(stack))


    

if __name__ == "__main__":
    word = "leet**cod*e"
    removeStars(word)