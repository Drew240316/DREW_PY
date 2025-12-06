# 전역 변수
scores = []

def add_score(name, score):
    # 지역 변수 name, score를 사용하여 전역 변수에 추가
    scores.append((name, score))

def print_scores():
    for name, score in scores:
        print(f"{name}의 점수는 {score}점입니다.")

def main():
    add_score("민지", 95)
    add_score("성수", 88)
    print_scores()

main()


#문법 요소	예시 코드	의미
#전역 변수	scores = []	모든 함수에서 접근
#지역 변수	name, score	add_score() 함수 내에서만 유효
#함수 호출 흐름	main() → add_score() → print_scores()	프로그램 흐름 구조 훈련
#리스트	scores.append(...)	자료 저장용 컬렉션 사용


# 입력 : 이름, 나이, 점수
# 출력 : 이름, 나이, 점수 입니다.
# 조건 : 여러명을 받는다. - 추가해야한다.리스트에서 , 출력할 때 여려명을 돌아가면서 출력한다.
# 출력받는 함수
# 입력받은 변수에서 여러명이 쌓이는 함수 (전역변수 필요 - 함수 바깥에서 가져오기 때문)
# 두 함수를 모두 실행하는 메인 함수
