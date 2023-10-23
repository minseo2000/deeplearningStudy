
''' 파일 압축 해제
import zipfile

DATA_PATH = '../../../kaggle_datasets/word2vec-nlp-tutorial/'
file_list = ['labeledTrainData.tsv.zip', 'unlabeledTrainData.tsv.zip', 'testData.tsv.zip']

for file in file_list:
    zipRef = zipfile.ZipFile(DATA_PATH+file, 'r')
    zipRef.extractall(DATA_PATH)
    zipRef.close()
'''

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = '../../../kaggle_datasets/word2vec-nlp-tutorial/'

# 데이터 불러오기
train_data = pd.read_csv(DATA_PATH+"labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
print(train_data.head())

# 히스토그램 그려보기 (x : 문장의 길이, y: 리뷰 수)
def show_histogram(train_data):
    plt.figure(figsize=(12, 5))
    plt.hist(train_data['review'].apply(len), bins=200, alpha=0.5, color='r', label='word')
    plt.yscale('log')
    plt.title('Length of review')
    plt.ylabel('Number of review')
    plt.show()

#박스 플롯 그리기
def show_boxPlot(train_data):
    plt.boxplot(train_data['review'].apply(len), labels=['counts'], showmeans=True)
    plt.show()

#show_histogram(train_data)
#show_boxPlot(train_data)

def show_wordcloud():
    from wordcloud import WordCloud
    cloud = WordCloud(width=400, height=300).generate("".join(train_data['review']))
    plt.figure(figsize=(20, 15))
    plt.imshow(cloud)
    plt.axis('off')
    plt.show()



