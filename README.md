# Waterlevel prediction (last update 2023.12.15)

## 한강 수위 예측 <br>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBae-ChangHyun%2FWaterlevel-predict&count_bg=%23113CD5&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 
<img alt="GitHub forks" src="https://img.shields.io/github/forks/Bae-ChangHyun/Waterlevel-predict">

프로젝트 기간: <br>
`개인`(2022.05 ~ 2023.05) <br>

### 1. Subject <br>
데이터 세트 한개를 이용하여 두가지 프로젝트 진행.
#### 1-1 Subject 1 
잠수교,한강대교,행주대교,청담대교 2023년 1~9월 수위(해발표고(El.m))를 선행시간 10분에 예측 
#### 1-2 Subject 2 
잠수교의 2023년 1~9월 수위(해발표고(El.m))를 선행시간에 따라 예측

프로젝트 회고 -> [블로그](https://changsroad.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%88%98%EC%9C%84%20%EC%98%88%EC%B8%A1)

### 2. Run <br>
1. `Collect_data.py`<br>
크롤링을 통해서 한강홍수통제소, 바다누리해양정보서비스에서 데이터를 수집. <br>
data_source.txt에 적혀있는 대교와 댐 데이터를 수집함<br>
code 폴더 안에 `.env` 파일을 생성하고 미리 api key를 입력해줘야 함.<br>

2. `Prepare_data.py` <br>
수집된 데이터를 적절한 형식으로 만들어주고 병합.<br>
data_source.txt에서 수집하고자하는 지점을 추가하는경우, 코드 내에서 튜닝(수위->해발표고)을 해줘야 함.<br>

3. `hangang_prediction.ipynb` <br>
수집된 데이터들을 이용하여 각종 EDA 및 전처리 모델 학습, 추론, 결과 도출<br>

4. `jamsu_leadtime_prediction.ipynb` -->아직 추가 안됨 <br>
잠수교 수위를 선행시간에 따라 모델 학습, 추론, 결과 도출 <br> 

### 3. Result <br>
미작성.

<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <br>
</div>
