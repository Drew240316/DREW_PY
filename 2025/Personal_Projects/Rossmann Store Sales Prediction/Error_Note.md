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
