

text_data = ['Hi!!!! I. Love. This. Song....',
             '10000% Agree!!!! #LoveIT',
             'Right?!?!']


# __ 위에 TEXT DATA는 삭제하지 마세요.__ 문제풀이용.


# 입력과 예상 출력 ? !!! . 과같은걸 모두 삭제하고 싶다.Hi I Love This Song
# 자료형 : 리스트 (순회) -> 리스트
# 모듈/클래스 - 함수 : dict - 프롬키즈 , 시스-유니코드데이터, 유니코드데이터-카테고리, 트랜스레이터 , chr , startwith()
# 딕셔너리로 변경하는 이유 : 맥시코드는 가장 큰 유니코드 표현 숫자로 조건문으로 구두점인 것을 찾아서 키 값으로 전달하면 된다.
# 키(유니코드 정수 포인트->문자->어떤 유니코드인지-그 유니코드 계열이 어딘지)
# 값은 (none) 형태.
# p로 시작하면 translate로 삭제한다.


import sys
import unicodedata
punctuation = dict.fromkeys( i for i in range(sys.maxunicode)

                            if unicodedata.category(chr(i)).startswith("P")
)

result = [ string.translate(punctuation)for string in text_data ]
print(result)
