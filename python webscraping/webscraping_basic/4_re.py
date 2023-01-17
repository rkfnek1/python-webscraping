import re
# ca?e

p = re.compile("ca.e") 
#.(ca.e) : 하나의 문자 > care, cafe, case (o) | caffe (x)
#^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
#$ (se$) : 문자열의 끝 > case, base (o) | face (x)

m = p.match("case")
#print(m.group()) # 매치되지 않으면 에러가 발생
if m :
    print(m.group())
else:
    print("매칭안됨")