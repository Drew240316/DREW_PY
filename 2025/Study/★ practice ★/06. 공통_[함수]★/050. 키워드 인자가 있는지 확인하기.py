def personal_info(**kwargs):
    """호출 시 키워드 인자를 받아 특정 키가 있는 경우에만 출력"""
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'adress' in kwargs:
        print('주소: ', kwargs['adress'])

personal_info(name = 'jessi')