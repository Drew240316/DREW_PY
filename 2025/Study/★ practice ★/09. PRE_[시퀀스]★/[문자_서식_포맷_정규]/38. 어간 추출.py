result2 = ['The', 'science', 'today', 'technology', 'tomorrow', '.', 'I', 'going', 'go', 'store', 'park']


from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()

porter = [ porter.stem(r) for r in result2]

print(porter)