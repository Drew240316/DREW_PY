
# 양쪽의 특정 문자 삭제하기
' , python. '.strip(' ,.')



# 구두점을 간단히 삭제하기 (string 모듈의 punctuation에는 모든 구두점이 들어있다. )
# !'"##$%^&*()_+"'

import string
' , python.'.strip(string.punctuation)


import string
# 파이썬 내장 함수 [문자_서식_포맷_정규](string)과 관련된 유용한 상수나 함수들을 제공해주는 표준 라이브러리

print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)           # 0123456789
print(string.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)       # 공백 문자들 (' \t\n\r\x0b\x0c')
