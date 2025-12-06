string = "The science of today is the technology of tomorrow.  I am going to go to the store and park"

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

result = word_tokenize(string)
print(result)

stop_words = stopwords.words('english') #영어 불용어 불러오기?
result2 = [ word for word in result if word not in stop_words ]
print(result2)