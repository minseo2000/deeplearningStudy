''' 데이터세트 다운로드
python -m spacy download en
'''

import spacy
nlp = spacy.load('en_core_web_sm')

sentence = "English Sentence"

print(nlp(sentence))