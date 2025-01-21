
def reverseWords( s):
        """
        :type s: str
        :rtype: str
        """
        print(s.split())
        
        # length = len(s)
        # word=[""]
        # skip = True
        # index = 0
        # for i in range(length):
        #     print('looking at',s[i], skip)
        #     if s[i] == " " and not skip :
        #          index+=1
        #          word.append("")
        #          skip = True
        #          continue
        #     elif s[i] == " " and skip:
        #          print('skipping this extra space')
        #          continue
        #     elif s[i] != " ":
        #          print('appending ', s[i], 'to index', index)
        #          word[index]+=(s[i])
        #          skip = False
        # # get the last space out
        # print(word)
        # if word[-1] == ' ':
        #     word= word[:-1]
        # word.reverse()
        # print(word, 'reversed')
        # for i in range(len(word)):
        #      print('/'.join(word))
        #      return(' '.join(word))
                    
                    
              

                
                    
                    

    

if __name__ == "__main__":
    s = "  hello world "
    reverseWords(s)