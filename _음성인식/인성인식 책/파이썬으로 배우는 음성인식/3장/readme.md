# 3장 음성처리 기초와 특징 추출

## JSUT[Sonobe 2017] 데이터 셋
- 여성화자 1명이 약 10시간 가량 발화한 음성이 수록된 무료 일본어 음성 데이터셋

### 용어 정리
| 용어      | 설명                                     |
|---------|----------------------------------------|
| 샘플링 주파수 | 1초간의 음성 음압치를 기록한 횟수                    |
| 음압      | 음파가 매질 속을 지날 때 매질의 각 질점에서 발생하는 압력의 변화량 |


- 일반적으로 16KHz 음성을 이용해 음성인식 실험을 진행한다.

- mp3 파일 -> 압축 파일, 정보손실 o 
- wav 파일 -> 비압축 파일, 정보손실x
- 마이크의 개수 -> 채널 (모노 or 스테레오)
- 파형 -> x, y로 음압을 표현
- 시간마다 순간 음압치를 기록 -> 샘플링 주기를 정해주어야 함.-> 역수를 취해 샘플링 주파수라고 함.
- 음압 방향도 기록해야 함.
- 

### 하는 일
1. 샘플링 주파수를 16KHz로 낮춘다. (다운 샘플링 작업)
2. 텍스트 파일을 문자, 단어 단위로 나누어 저장하기
3. 학습 데이터, 개발 데이터, 평가 데이터로 분리
4. 음성 파형을 시각화
5. 코드 분석


### Codes

1. 음원 데이터 시각화 하기
```
import wave
import numpy as np
import matplotlib.pyplot as plt

wav_file = ''
output = ''

with wave.open(wav_file) as wav:
    sampling_frequency = wav.getframerate() # 샘플링 주파수 확인
    sample_size = wav.getsampwidth() # 샘플 사이즈 확인
    num_channels = wav.getnchannels() # 채널 수 확인
    num_samples = wav.getnframes() # wav 데이터 샘플 수 확인
    waveform = wav.readframes(num_samples) # wav 데이터 읽기
    waveform = np.frombuffer(waveform, dtype=np.int16) # 바이너리 to int16 변환


```