import pandas as pd

# CSV 불러오기
df = pd.read_csv("C://Users//wkdal//Desktop//test_3.csv")

# JSON으로 저장 (확장자도 .json으로!)
df.to_json("C://Users//wkdal//Desktop//to_json.json", orient="records", force_ascii=False, indent=2)
