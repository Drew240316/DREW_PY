# 정규표현식(re)는 1. 문자열에서 특정한 규칙으로 된 문자열을 검색하고 추출 2. 문자열이 정해진 규칙에 맞는지 판단할 때 사용

# 2 - 문자열 판단
    # re모듈의 match함수 사용
    # re.match('패턴','문자열') 문자열에 해당 패턴이 있는지 판단
    # <_sre.SRE_Match.objects;> 객체가 반환됨.
import re
x = re.match('Hello','Hello, world' )
print(x)

# 2 - 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단.
    # ^문자열
    # 문자열$
    # search 함수 사용.
    # re.search('패턴','문자열')

y = re.search('^Hello','HelloWorld')  # Hello로 시작하므로 패턴에 매칭됨
print(y)

y2 = re.search('Hello$','HelloWorld')
print(y2)                                        # world!로 끝나므로 패턴에 매칭안됨 -> none

# 2- 지정된 문자열이 하나라도 있는지 판단.

    #|는 특정 문자열에서 지정된 문자열(문자)이 하나라도 포함되는지 판단한다. 기본 개념은 or이다
    # 문자열|문자열 로 씀.
z = re.match('hello|world','hello')
print(z)