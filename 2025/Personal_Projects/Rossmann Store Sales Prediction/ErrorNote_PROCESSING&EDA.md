ModuleNotFoundError: No module named 'sklearn'
ModuleNotFoundError: No module named 'sklearn'

!pip install scikit-learn

</details> <details> <summary><strong>AttributeError</strong></summary>
AttributeError: 'NoneType' object has no attribute 'rename'
AttributeError: 'NoneType' object has no attribute 'rename'


columns를 꼭 쓰기

store = store.rename(
    columns = {
        "Store" : "매장ID",
        "StoreType" : "매장유형",
    },
    inplace = True
)

AttributeError: 'Index' object has no attribute 'year'
AttributeError: 'Index' object has no attribute 'year'


DatetimeIndex가 아니면
index.year, index.month, index.day, index.isocalendar().week 같은 날짜 관련 속성을 사용할 수 없다.

따라서 날짜 컬럼을 인덱스로 변환해 날짜 타입으로 만들고, 추출한다.

train['연도'] = train.index.isocalendar().year
train['월'] = train.index.month
train['일'] = train.index.day
train['주'] = train.index.isocalendar().week
train.head()

날짜 기반 인덱스(DateTimeIndex)와 날짜 구성요소 추출
1) index

DataFrame의 인덱스가 날짜형(DatetimeIndex)일 때 사용 가능한 날짜 속성 접근자.
예시: DatetimeIndex(['2015-07-31', '2015-07-30', ...])

2) isocalendar()

ISO-8601 국제 표준 달력 방식으로 날짜를 연도(ISO Year), 주차(ISO Week), 요일(ISO Weekday)로 변환한다.
여기서 week = 31 은, "2015년의 31번째 주(31주차)"

AttributeError: 'function' object has no attribute 'sum'
AttributeError: 'function' object has no attribute 'sum'


train.isnull.sum()에서 train.isnull().sum()로 고친다.
괄호 = 실행, isnull = 함수명 → 실행하지 않아 오류 발생.

AttributeError: 'DataFrame' object has no attribute 'type'
AttributeError: 'DataFrame' object has no attribute 'type'


DataFrame 전체 type 확인:

train.info()

</details> <details> <summary><strong>ValueError</strong></summary>
ValueError: Cannot subset columns with a tuple with more than one element. Use a list instead.
ValueError: Cannot subset columns with a tuple with more than one element. Use a list instead.

train_store_joined.groupby('매장유형')['방문고객수','예상매출액','고객당평균매출'].sum().sort_values('예상매출액', ascending='desc')


한글일 경우
['방문고객수','예상매출액','고객당평균매출'] 이 리스트가 아니라 튜플로 인식됨.

✔ 컬럼 여러 개 선택 시 반드시 리스트 사용

ValueError: For argument "ascending" expected type bool, received type str.
ValueError: For argument "ascending" expected type bool, received type str.

train_store_joined.groupby('매장유형')[['방문고객수','예상매출액','고객당평균매출']].sum().sort_values('예상매출액', ascending='desc')


ascending은 True/False 값이어야 함.
문자열 'desc' 를 넣어 오류 발생.

✔ 해결:

.sort_values('예상매출액', ascending=True)

</details> <details> <summary><strong>📌 sns.catplot() 파라미터 정리</strong></summary>
sns.catplot 파라미터 정리
sns.catplot(
    data=..., x=..., y=..., hue=..., col=..., row=..., kind=..., height=..., aspect=...
)

1) data

사용할 데이터프레임
예: data=train_store_joined

2) x

x축 컬럼
예: '월', 'DayOfWeek'

3) y

y축 컬럼
예: '예상매출액', 'Sales'

4) hue

색상 기준
예: '프로모션여부'

5) col

열 방향 비교
예: col='StoreType'

6) row

행 방향 비교
예: row='연도'

7) kind

사용 가능한 그래프 종류
(strip, swarm, box, violin, boxen, point, bar, count)

예: kind='point' → 평균 기반 점 + 선 그래프

8) height

그래프 세로 크기(inch)

9) aspect

가로 비율 → 가로 = height × aspect

예시 코드
sns.catplot(
    data=train_store_joined_open,
    x='월',
    y='예상매출액',
    hue='상시프로모션참여여부',
    col='(1차)프로모션시행여부',
    row='연도',
    kind='strip',
    height=4,
    aspect=1.2
)

</details> ```
