
def reverseVowels( s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        # List of vowels
        vowels = ('a','e', 'i','o', 'u','A','E','I','O','U')
        reversed_string = list(s)
     
        
        # scan the string from both ends using two counters and swap everytime we have two vowels , we stop when we cross over
        while left<right:
            print('left', left, 'right', right, reversed_string)
            #search for vowel from  left
            while left < right and reversed_string[left] not in vowels:
                left+=1
            while left<right and reversed_string[right] not in vowels:
                right-=1
            if left<right:
                temp = reversed_string[left]
                reversed_string[left] = reversed_string[right]
                reversed_string[right] = temp
                print('swapped', left , right, reversed_string)
                left+=1
                right-=1
        print("".join(reversed_string))
        print(s)

                
                    
                    

    

if __name__ == "__main__":
    s = "a.b,."
    reverseVowels(s)