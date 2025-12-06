<details>
<summary><strong>ImportError</strong></summary>
# ImportError: cannot import name 'arima' from 'statsmodels.tsa.arima_model' 
  
  import 시, arima > ARIMA로 수정
</details>


<details>
<summary><strong>ModuleNotFoundError</strong></summary>
# ModuleNotFoundError: No module named 'sklearn'
  
  !pip install scikit-learn
# ModuleNotFoundError: No module named 'fbprophet'

</details>



<details>
AttributeError: 'NoneType' object has no attribute 'rename'

   columns를 꼭 쓰기
   store = store.rename(columns = {
    "Store" : "매장ID",
    "StoreType" : "매장유형",
}
,inplace = True)
  
</details>


<details>
AttributeError: 'Index' object has no attribute 'year'
날짜 타입인 인덱스를 사용해야、 인덱스에서 요일 월 일 주 추출 가능.

train['연도'] = train.index.isocalendar().year
train['월'] = train.index.month
train['일'] = train.index.day
train['주'] = train.index.isocalendar().week
train.head()
</details>


