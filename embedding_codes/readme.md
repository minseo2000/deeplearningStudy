# 임베딩을 사용한 감성 프로그래밍

## 임베딩이란?

### 단어의 의미 구축하기

1. ex) 기사의 헤드라인 속 모든 단어를 양수로 인코딩, 정상적인 헤드라인의 단어를 음수로.


2. ex) 성별을 x축, 귀족을 y축, 등장인물의 재산을 벡터의 길이로 나타낼 수 있다.

## 텐서플로의 임베딩
- 단어의 벡터를 만들고, 해당 벡터가 비슷하면, 비슷한 의미를 갖을 것이다.

### 임베딩을 사용해 빈정거림 감지기 만들기




# Codes Description
| 코드                 | 아웃풋 | 설명                             |
|--------------------|-----|--------------------------------|
| str.maketrans      |<img width="400" alt="maketrans" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/e0d1df44-a9e3-43de-92ed-822dad6433d4">| 1인자에서 2인자로 대치하는데, 3인자를 제외하고 대치 |
| string.punctuation | <img width="400" alt="string punctuation" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/cda131ef-95a3-4a2a-89d6-e250da2ec28a">| 특수 기호 목록 출력                    |
| json.load()        |     | json파일을 로드함.                   |
| get_text()         | <img width="400" alt="get_text" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/a9db63d5-64b2-4534-8207-5e8d8406e1ad">| html 태그를 제거해서 출력함              |


# 요약서
| ?       | 설명            | example_Data             |
|---------|---------------|--------------------------|
| Problem | 빈정대는 헤드라인 감지기 |                          |
| Dataset | 'sarcasm.json' | {"headlide" : "sentece"} |

## 데이터 전처리 과정
| 작업                                                       | 설명              | 이미지 결과 |
|----------------------------------------------------------|-----------------|--------|
| 데이터 로딩                                                   | json에서 데이터를 가져옴 |        |
| 불용어 정의                                                   | 불용어를 모두 제거한다.   |        |
| 소문자로 변환<br/>","->" , "<br/>"." -> " . "<br/>"/" -> " / " | 문자 통일           |        | 
| html 태그 제거                                               | 태그 불필요          |        |
| 토큰화 및 시퀀스로 만들기                                           | 단어장 만든다.        |        |
| 모델에 넣기                                                   | 학습 모델에 넣기       ||