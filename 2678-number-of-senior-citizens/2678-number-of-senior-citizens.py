class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for detail in details:
            age = detail[11:13]
            if int(age)>60:
                cnt+=1
        return cnt
        