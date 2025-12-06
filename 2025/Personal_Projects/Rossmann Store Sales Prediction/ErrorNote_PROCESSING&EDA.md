📘 Kaggle EDA 중 발생하는 Python 오류 & 해결 모음
📑 전체 오류 목록 (TOC)

아래 오류명을 클릭하면 상세 위치로 이동합니다.

ImportError

ImportError: cannot import name 'arima'

ModuleNotFoundError

ModuleNotFoundError: No module named 'sklearn'

AttributeError

AttributeError: 'NoneType' object has no attribute 'rename'

AttributeError: 'Index' object has no attribute 'year'

AttributeError: 'function' object has no attribute 'sum'

AttributeError: 'DataFrame' object has no attribute 'type'

ValueError

ValueError: Cannot subset columns with a tuple

ValueError: ascending expected bool but str received

Seaborn Reference

sns.catplot() 파라미터 설명

🔽 상세 설명
ImportError
<details> <summary><strong>ImportError: cannot import name 'arima'</strong></summary>
🔗 앵커: <a id="importerror-cannot-import-name-arima"></a>
ImportError: cannot import name 'arima' from 'statsmodels.tsa.arima_model'

✔ 원인

statsmodels는 arima(소문자)가 아닌 ARIMA(대문자) 사용.

✔ 해결
from statsmodels.tsa.arima_model import ARIMA

</details>
ModuleNotFoundError
<details> <summary><strong>ModuleNotFoundError: No module named 'sklearn'</strong></summary>
🔗 앵커: <a id="modulenotfounderror-no-module-named-sklearn"></a>
ModuleNotFoundError: No module named 'sklearn'

✔ 해결
!pip install scikit-learn

</details>
AttributeError
<details> <summary><strong>AttributeError: 'NoneType' object has no attribute 'rename'</strong></summary>
🔗 앵커: <a id="attributeerror-nonetype-object-has-no-attribute-rename"></a>
AttributeError: 'NoneType' object has no attribute 'rename'

✔ 원인

rename(..., inplace=True)는 return 값이 None → 변수에 저장하면 NoneType.

✔ 해결
store.rename(
    columns={
        "Store": "매장ID",
        "StoreType": "매장유형"
    },
    inplace=True
)

</details>
<details> <summary><strong>AttributeError: 'Index' object has no attribute 'year'</strong></summary>
🔗 앵커: <a id="attributeerror-index-object-has-no-attribute-year"></a>
AttributeError: 'Index' object has no attribute 'year'

✔ 원인

.year, .month, .day, .isocalendar().week 등은 DatetimeIndex에서만 사용 가능.

✔ 해결
train.index = pd.to_datetime(train['Date'])

train['연도'] = train.index.isocalendar().year
train['월']   = train.index.month
train['일']   = train.index.day
train['주']   = train.index.isocalendar().week

</details>
<details> <summary><strong>AttributeError: 'function' object has no attribute 'sum'</strong></summary>
🔗 앵커: <a id="attributeerror-function-object-has-no-attribute-sum"></a>
AttributeError: 'function' object has no attribute 'sum'

✔ 원인

함수 isnull 자체를 실행하지 않고 .sum() 호출함.

✔ 해결
train.isnull().sum()

</details>
<details> <summary><strong>AttributeError: 'DataFrame' object has no attribute 'type'</strong></summary>
🔗 앵커: <a id="attributeerror-dataframe-object-has-no-attribute-type"></a>
AttributeError: 'DataFrame' object has no attribute 'type'

✔ 해결

전체 타입 확인은 .info() 사용:

train.info()

</details>
ValueError
<details> <summary><strong>ValueError: Cannot subset columns with a tuple with more than one element. Use a list instead.</strong></summary>
🔗 앵커: <a id="valueerror-cannot-subset-columns-with-a-tuple-with-more-than-one-element-use-a-list-instead"></a>
ValueError: Cannot subset columns with a tuple with more than one element. Use a list instead.

✔ 문제 코드

한글 컬럼명을 ['a','b','c']로 쓰면 tuple로 인식되는 경우 있음.

train_store_joined.groupby('매장유형')['방문고객수','예상매출액','고객당평균매출'].sum()

✔ 해결
train_store_joined.groupby('매장유형')[['방문고객수','예상매출액','고객당평균매출']].sum()

</details>
<details> <summary><strong>ValueError: For argument "ascending" expected type bool, received type str.</strong></summary>
🔗 앵커: <a id="valueerror-for-argument-ascending-expected-type-bool-received-type-str"></a>
ValueError: For argument "ascending" expected type bool, received type str.

✔ 문제 코드
sort_values('예상매출액', ascending='desc')  # ❌ 문자열 str

✔ 해결
sort_values('예상매출액', ascending=True)

</details>
Seaborn 참고
<details> <summary><strong>📌 sns.catplot 파라미터 정리</strong></summary>
🔗 앵커: <a id="-sns-catplot-파라미터-정리"></a>
기본 문법
sns.catplot(
    data=..., 
    x=..., 
    y=..., 
    hue=..., 
    col=..., 
    row=..., 
    kind=..., 
    height=..., 
    aspect=...
)

주요 파라미터 설명

data: 사용할 DataFrame

x: x축 컬럼

y: y축 컬럼

hue: 색상 구분

col: 열 방향 subplot

row: 행 방향 subplot

kind: strip / swarm / box / violin / point / bar / count

height: 세로 크기

aspect: 가로 비율 (가로=height×aspect)

예시
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

</details>
