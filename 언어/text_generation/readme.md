# 텍스트 생성하기

## 문제 : 입력 시퀀스와 레이블로 -> 시퀀스를 변환해야한다!
## 문제2 : 입력 시퀀스는 단어의 그룹, 레이블을 문장 안에 있는 다음 단어.

- Example
```commandline
Sentence = "Today has a beautiful blue sky"
-> 입력 시퀀스 + 다음단어 레이블로 변환하라하면 다음과 같이 한다.
enter_sequence = "Today has a beautiful blue"
label = "sky"
```

- 위 작업을 해주는 코드

```commandline
input_sequence = []
for lien in corpus:
    token_list = tokenizer.texts_to_sequnces([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequnce = token_list[:i+1]
        input_sequences.append(n_gram_sequence)
```
- 위 작업에 대핸 결과 예시
```commandline
example_sentence = "Today has a beautiful blue sky"
-> 토크나이징
example_sequence = "[1, 5, 6, 7, 8, 9]
-> 입력 시퀀스 + 레이블

1. example_enter_sequence = [1]
2. example_enter_sequence = [1, 5]
3. example_enter_sequence = [1, 5, 6]
4. example_enter_sequence = [1, 5, 6, 7]
5. example_enter_sequence = [1, 5, 6, 7, 8]
6. example_enter_sequence = [1, 5, 6, 7, 8, 9]
-> 패딩 작업 + label 선언 (label은 입력 시퀀스의 마지막 토큰으로 한다.
1. example_enter_sequence = [0,0,0,0,0,1]    , label = [1]
2. example_enter_sequence = [0,0,0,0,1, 5]   , label = [5]
3. example_enter_sequence = [0,0,0,1, 5, 6]  , label = [6]
4. example_enter_sequence = [0,0,1, 5, 6, 7] , label = [7]
5. example_enter_sequence = [0,1, 5, 6, 7, 8], label = [8]
6. example_enter_sequence = [1, 5, 6, 7, 8, 9], label = [9]
```

- model Description <br>
모델은 다음 단어를 예측하는 것이다. <br>
즉, 입력 시퀀스가 주어지면 다음 단어를 예측하는 것으로 다음과 같다.
```commandline
enter_sequence = "Today is a very"  -> model -> output : hot. => "Today is a very Hot"
enter_sequence2 = "Today is a very Hot" -> model -> output : so => "Today is a very Hot so"
```
위 와 같은 방식으로 문장을 생성해낸다.

## 문자 기반 인코딩
- 단어 기반 인코딩에서 문자기반 인코딩으로 무슨말이냐?
```commandline
안녕하세요 -> 한단어
안녕하세요 -> 5개의 문자 "안" "녕" "하" "세" "요"
```

위에서 하던 방법을 문자기반으로 바꾼다면, 단어는 무수히 많지만, 문자는 그 개수가 정해져 있어 모델이 한 층 더 작어진다.<br>
왜? 출력층의 뉴련의 개수가 줄어드는 것임.
