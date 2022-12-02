from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a=Counter(word1)
        b=Counter(word2)
        #print(a,b)
        a_list=[v for k,v in a.items()]
        b_list=[v for k,v in b.items()]
        a_list.sort()
        b_list.sort()
        if a_list==b_list and set(word1)==set(word2):
            return True 
        return False