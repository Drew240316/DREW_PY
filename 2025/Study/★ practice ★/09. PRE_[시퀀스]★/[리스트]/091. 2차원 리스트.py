# sorted(iterable, key=None, reverse=False)
# sorted(이터러블, 키 = 정렬할 함수, reverse= true는 내림차순 false 오름차순)
# 함수 : key=len, key=str.lower , key= str, upper

# 1. 기본 정렬
sorted([3, 1, 2])  # → [1, 2, 3]

# 2. key 사용
words = ['banana', 'apple', 'cherry']
sorted(words, key=len)  # → ['apple', 'banana', 'cherry']

# 3. reverse 사용
sorted([3, 1, 2], reverse=True)  # → [3, 2, 1]

# 4. 학생 정보가 저장된 2차원 리스트 활용
students = [
    [ 'john', 'C', 19 ],
    [ 'maria', 'A', 25 ],
    [ 'andrew', 'B', 7 ]
]

print(sorted(students, key = lambda student : student[2]))
# lambda student: student[2]는
# 각 학생 리스트에서 나이만 꺼내서 그걸 기준으로 정렬해줘