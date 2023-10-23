''' 데이터세트 다운받기
import nltk
nltk.download()
'''


from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "English Sentence"

print(word_tokenize(sentence))
print(sent_tokenize(sentence))