<details>
<summary><strong>ImportError</strong></summary>
# ImportError: cannot import name 'arima' from 'statsmodels.tsa.arima_model' 
  
  import 시, arima > ARIMA로 수정
</details>








<details>
<summary><strong>ModuleNotFoundError</strong></summary>
# ModuleNotFoundError: No module named 'sklearn'
  
  !pip install scikit-learn

</details>








<details>

  # AttributeError: 'NoneType' object has no attribute 'rename'

   columns를 꼭 쓰기
   store = store.rename(columns = {
    "Store" : "매장ID",
    "StoreType" : "매장유형",
   }
   ,inplace = True)



  # AttributeError: 'Index' object has no attribute 'year'
  `DatetimeIndex`가 아니면  
  `index.year`, `index.month`, `index.day`, `index.isocalendar().week`  
   같은 날짜 관련 속성을 사용할 수 없다.

   따라서 날짜 컬럼을 인덱스로 변환해 날짜 타입으로 만들고, 추출한다.

  train['연도'] = train.index.isocalendar().year
  train['월'] = train.index.month
  train['일'] = train.index.day
  train['주'] = train.index.isocalendar().week
  train.head()

  ### 날짜 기반 인덱스(DateTimeIndex)와 날짜 구성요소 추출

  #### 1) `index`
  DataFrame의 인덱스가 날짜형(`DatetimeIndex`)일 때 사용 가능한 날짜 속성 접근자.
  예시:DatetimeIndex(['2015-07-31', '2015-07-30', ...])
  #### 2) `isocalendar()`
  ISO-8601 국제 표준 달력 방식으로 날짜를 연도(ISO Year), 주차(ISO Week), 요일(ISO Weekday)로 변환한다.
  여기서 week = 31 은, "2015년의 31번째 주(31주차)"


  # AttributeError: 'function' object has no attribute 'sum'
  train.isnull.sum()에서 train.isnull().sum()로 고친다.
  괄호 = 실행, isnull = 함수명 이므로, 앞에서 함수를 실행하지 않아서 오류가 났다.




  
</details>


