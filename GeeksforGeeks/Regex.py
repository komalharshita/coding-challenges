import re
def numberMatcher(str):
    pat= r"\d+"
    match=re.findall(pat,str)
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")