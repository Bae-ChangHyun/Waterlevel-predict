# Waterlevel prediction (last update 2023.10.23)
2023년 잠수교 수위 예측 (1월 ~ 9월) <br>

├── data
│   ├── 2023_answer.csv : 2023년 잠수교 수위
│   ├── full_data.csv: 2013~2023 모든 feature,target 데이터
│   └── ppd_data.csv: 전처리가 완료된 데이터 
├── code
│   ├── 0.Full.ipynb : 데이터 수집을 제외한 전체 코드
│   ├── 1. Collect_data.py: 데이터 수집
│   ├── 2. Prepare_data.py: 수집된 데이터 병합 및 후처리
│   ├── 3. EDA.ipynb: 데이터 eda, 전처리, feature engineering
│   ├── 4. Modeling.ipynb: 선행시간에 따른 2023년 잠수교 수위 예측
│   └──data_source.txt: 수집하고자하는 데이터 목록
├── result
│   ├── leadtime(n)
│   │   ├── final_model-1.csv: 전체월로 학습한 모델로 예측
│   │   ├── final_model-2.csv: 비홍수기로 학습한 모델로 예측
│   │   ├── final_model-3.csv: 홍수기로 학습한 모델로 예측
└── └── └── lt(n)_predict.csv: 가장 성능이 좋은 예측 최종 결과


* * * * * * * * *

## [1. Collect_data.py]

- Origin 데이터수집- api를 이용한 크롤링 방식

  <b>유의사항</b> <br>
  -> 미리 한강홍수통제소, 바다누리 해양정보서비스의 API키를 발급받아야 함.<br>
  -> 입력받을 시 오타 입력시 경고없이 종료됨.<br>
  -> 모든 데이터는 10분간격의 데이터로 수집됨.<br>
  -> 현재 디렉토리 하위에 data라는 폴더를 생성하고 아래 폴더명으로 파일 자 생성됨.<br>
  -> 년,월 별로 파일이 개별 생성 이후 다음 Preprocessisng_data.py를 이용하여 병합해야함.<br>
  -> 현재 년, 월 이후를 입력시 오류 발생(추후 입력불가하게 수정예정)<br>
  -> 다른 지점의 데이터를 수집하려면, 폴더 내 data_source.txt에 동일 형식으로 추가해주면 됨.<br>
  
  - 한강홍수통제소(https://hrfco.go.kr/main.do)<br>
      - data/bridge/ <br>
          잠수교, 청담대교, 한강대교, 행주대교, 광진교, 팔당대교, 중랑교 수위 및 유량 <br>
      - data/data/ <br>
          팔당댐 수위, 유입량, 저수량, 공용량, 방류량 <br>
      - data/rf/ <br>
          대곡교, 진관교, 송정동 강수량 <br>
  
  - 바다누리해양정보서비스(http://www.khoa.go.kr/oceangrid/khoa/intro.do) <br>
      - data/tide/ <br>
          강화대교 조위 <br>

## [2. Preprocessing_data.py] <br>

- Origin 데이터 병합 <br>

<b>유의사항</b> <br>
-> 미리 1. Collect_data.py를 이용하여 데이터를 수집해야함.(경로 변경x) <br>
-> 입력받을 시 오타 입력시 경고없이 종료됨. <br>
-> 기본 제공 지점 외 다른 지점을 추가로 수집했을 경우 py내 def preprocessing에서 수위->해발표고 변환 값을 튜닝해줘야 함.(한강홍수통제소 참고)  <br>
-> 기본적으로 년,월로 나눠있는 데이터들을 병합. <br>

## [3. EDA.ipynb] <br>

- 데이터 EDA <br>

<b>EDA</b> <br>
-> 잠수교 인근 대교들과의 수위 비교.
-> 대교들의 흐름 파악(하류에 있는 수위가 먼저 변함. 전류리>한강대교>행주대교>잠수교~)
-> 년,월별 잠수교의 수위 추세 확인(특정 월, 특정 년에 잠수교의 수위가 높음)

<b>Preprocessing</b> <br>
-> 각 데이터들의 이상치 제거
-> 결측치가 50% 이상 및 다중공산성 발생하는 column 제거
-> 이전 30분의 이동평균을 이용하여 결측치 제거

<b>Feature engineering</b> <br>
-> hour, month 컬럼 추가
-> 잠수교 변화율 컬럼 추가

## [4. Modeling.ipynb] <br>

- 최종 예측 <br>

<b>Modeling</b> <br>
-> 선행시간을 입력하면, 2023년 잠수교 수위를 예측
-> 선행시간 값 자유로이 추가 가능

## [5. Modeling.ipynb] <br>

- 통합본 <br>

<b>Full</b> <br>
-> 데이터 수집을 제외한 eda 및 modeling 실험이 포함되어 있음.