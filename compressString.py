def compress(chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #begin with empty string s
        s =[]
        length = len(chars)
        count=0
        append_count = []
        # walk through chars counting repeating characters
        for i in range(length):
            #print(i, 'iteration', 's =',s)
            if not s:
                 s.append(chars[i])
                 count=1
                 #print('s was empty appended and set count', 's =',s, 'count=', count)
            elif chars[i] == s[-1]:
                 count+=1
                 #print('repeat character', chars[i], 's =',s, 'count=', count)
            elif (chars[i] != s[-1]) or (i == length -1) :
                 #print('non repeating character or last character', chars[i], 's =',s, 'count=', count)
                 if count > 1:
                     for digit in str(count):
                        s.append(digit)
                         
                         
                 count=1
                 s.append(chars[i])
                 #print('reset count and added character to s', chars[i], 's =',s, 'count=', count)  
                 
        if count > 1:
            for digit in str(count):
                 s.append(digit)
            
        # s.append(str(count))
        #print('done with iterations, added the count to s', chars[i], 's =',s, 'count=', count)
        chars[:] = s
        
        print('chars', chars)
        #print(len(s))

            
            
                    
              

if __name__ == "__main__":
    s = ["a","a","b","b","b","b","b","b","b","b","b","b","b","b", "c", "c", "c"]
    compress(s)