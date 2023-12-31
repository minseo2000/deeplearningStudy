# 분류문제 실제로 해보기

## 감정 분류 문제를 다뤄보겠다. 주어진 글을 분석한 후 감정을 긍정 혹은 부정으로 예측하는 모델을 만들 것이다.

## 결과: 새로운 리뷰가 긍정적인 리뷰인지 부정적인 리뷰인지 예측하게 될 것이다.


## 문제 해결 과정

| 단계    | 하는 일         |
|-------|--------------|
| 1. 단계 | 데이터 전처리하기    |
| 2. 단계 | 데이터 분석하기     |
| 3. 단계 | 알고리즘을 모델링 하기 |

## 데이터 분석단계

| 방법               | 설명                                         |
|------------------|--------------------------------------------|
| 히스토그램 그리기        | x좌표에 문장길이를 설정해서, 문장 길이가 다른 데이터의 분포를 확인해보자. |
| 박스 플롯 생성         | 문장길이의 분포를 좀 더 잘 볼 수 있다.                    |
| word2cloud 라이브러리 | 가장 많이 사용된 순으로 문자의 크기를 그림으로 보여준다.           |
| 히스토그램 그리기        | x좌표에 문자 개수를 설정해서, 문장마다 단어의 개수를 세어준다. p158      | 

