string = "The science of today is the technology of tomorrow"

# 단어 토큰화 하려면?
# 모듈/클래스 - 함수 ?   nltk.tokenize  - word_tokenize



from nltk.tokenize import word_tokenize

result = word_tokenize(string)
print(result)
