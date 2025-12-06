x = 10  # 전역 변수 정의

def foo():
    global x
    print(x)        # 여기서 출력: 전역 x = 10

foo()              # 함수 호출: 전역 x(10) 출력
print(x)           # 함수 밖에서 다시 전역 x 출력



#foo() 안의 print(x)	global x로 전역변수 x를 참조해서 출력	10
#마지막 줄 print(x)	함수 밖에서 전역변수 x 그대로 출력	10