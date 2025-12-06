def personal_info(name, **kwargs):
    """ 고정인수 name과 가변 키워드 인수를 모두 사용하기
        - 가변 키워드 인수라 딕셔너리 언패킹 가능 """
    print(name)
    print(kwargs)

personal_info('홍길동', age = 30, address = '서울시 용산구')
personal_info(**{'name':'홍길동', 'age':30})

print()
print(personal_info.__doc__)


