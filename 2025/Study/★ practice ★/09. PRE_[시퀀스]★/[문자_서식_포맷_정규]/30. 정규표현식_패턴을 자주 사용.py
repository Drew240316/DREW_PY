# match나 search 함수에 정규표현식 패턴을 지정하는 방법은 비효율적입니다.
# 같은 패턴을 자주 사용할 때는 compile 함수를 사용해서 정규표현식 패턴을 객체로 만든 뒤,match 또는 search 메서드를 호출합니다.
    # 객체 = re.compile('패턴')
    # 객체.match('문자열')
    # 객체.search('문자열')

import re
x = re.compile('[0-9]+') # 정규표현식 패턴을 객체로 만듬
x.match('12345')
x.search('12345')