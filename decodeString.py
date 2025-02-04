
def decodeString( string):
    """
    :type string:str
    :rtype: str
    algo:
    - make 3 stacks , multiplier - holds digits , pattern - holds patterns, result = holds the answer
    - start scan
        - if it is digit, put into the mutliplier stack. we use a flag to ensure that multiple digits can be accounted for.
        - if it is left square bracket, assign empty element into the pattern stack, we will have as many slots as [ seen without the closing ].
        - we add characters to pattern stack till we encounter the closing ] . 
            - pop the pattern stack and multiplier stack, and append the resulting string to result
            - if pattern is not empty, we append this string from result to the string left in pattern stack.
    """
    
    print(string)
    multiplier, pattern, result = list(), list(),list()
    lastCharDigit = False
    for char in string: 
        if char.isdigit():
            if lastCharDigit:
                multiplier[-1] = multiplier[-1]*10 + int(char)
            else:
                multiplier.append(int(char))
                lastCharDigit = True
        elif char == '[':
            pattern.append('')
            lastCharDigit = False
        elif char ==']':
            result.append(pattern[-1]* multiplier[-1])
            pattern.pop()
            multiplier.pop()
            if pattern:
                pattern[-1]+=result[-1]
                result.pop()
        elif pattern:
            pattern[-1]+=char
        else:
            result.append(char)
        print('parsing', char, 'pattern',pattern, 'multiplier',multiplier, 'result', result)

    print(''.join(result))

if __name__ == "__main__":
    string = "3[a2[c]]" 
    decodeString(string)