# format 메서드로 값을 여러개 넣기

'Hello, {0} {2} {1}'.format('python', 'script', 3.6)


# -> 인덱스 생략 가능하다.
'Heloo, {} {} {}'.format('Python','Script', 3.6)



# -> 이름 지정 가능하다.

'Hello. {language} {version} '.format(language='Python')


# -> 변수를 사용해도 된다.

language = 'python'
version  = 3.6

f'Hello World, {language} {version}'
