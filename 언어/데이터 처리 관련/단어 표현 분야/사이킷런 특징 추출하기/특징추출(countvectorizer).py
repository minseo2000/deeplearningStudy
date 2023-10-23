from sklearn.feature_extraction.text import CountVectorizer


text_data = ['나는 배가 고프다', '내일 점심 뭐먹지?', '내일 공부 해야겠다.', '점심 먹고 공부 해야지']

count_vectorizer = CountVectorizer()
count_vectorizer.fit(text_data)

단어사전 = sorted(count_vectorizer.vocabulary_.items(), key=lambda x:x[1])
print(단어사전)

print(count_vectorizer.transform(['안녕 나는 나는 배가 고프다']).toarray())