def maxVowels( s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        algo:
        sliding window of k size , keeping track of number of distinct vowels seen in any of the windows
        we compare the outgoing index at current left - 1 , to see if it was a vowel or not similar for included element at current right. if both are vowels, we move on else, we adjust the vowel count accordingly

        """
        left = 0 
        right = k - 1
        vowels =('a', 'e', 'i', 'o', 'u')
        max_vowels = 0
        
        #1st window
        for i in range(left, right+1):
            if s[i] in vowels:
                max_vowels+=1
        print('vowels in first window is ',max_vowels)

        window_vowels = max_vowels
        # increment pointer to next window boundaries
        left+=1
        right+=1

        while right < len(s):
            # check if outgoing item was a vowel and same for incoming item, if both are vowels, max vowel doesn't change. the count only changes if incoming is a vowel and outgoing is not a vowel
            print('examining window ', s[left:right+1], 'max vowels is ', max_vowels)
            if s[left-1] not in vowels and s[right] in vowels:
                 
                 window_vowels+=1 
                 print('increasing window vowels', window_vowels)
            # if outgoing is a vowel and incoming is not, then the sliding window loses a vowel and we need to adjust
            if s[left-1] in vowels and s[right] not in vowels:
                 window_vowels-=1
            if window_vowels > max_vowels:
                 max_vowels = window_vowels
            left+=1
            right+=1
        print(max_vowels)
            
              
              






if __name__ == "__main__":
    s="ppuuoibwiogewxvgxvugwatxebstgdciswnkynvsbktfrrzxddzpjzvmqnjigkyviwoniyfkhadnqgihbobjjgcmmmnqzsckkqnfonepbgvzrnwxlrdawkwwbnwfouofdtskznfglbsfdaulxj"
    k = 20
    maxVowels(s, k)