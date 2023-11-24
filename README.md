# Waterlevel prediction (last update 2023.10.23)

## 2023년 잠수교 수위 예측 (1월 ~ 9월) <br>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBae-ChangHyun%2FWaterlevel-predict&count_bg=%23113CD5&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 
<img alt="GitHub forks" src="https://img.shields.io/github/forks/Bae-ChangHyun/Waterlevel-predict">

프로젝트 기간: <br>
`개인`(2022.05 ~ 2023.05) <br>

### 1. Subject <br>
잠수교의 2023년 수위(해발표고(El.m))를 선행시간에 따라 예측하는 프로젝트

프로젝트 회고 -> [블로그](https)

### 2. Run <br>
1. `Collect_data.py`<br>
크롤링을 통해서 한강홍수통제소, 바다누리해양정보서비스에서 데이터를 수집. <br>
data_source.txt에 적혀있는 대교와 댐 데이터를 수집함<br>
.env파일을 생성하고 미리 api key를 입력해줘야 함. wiki 참조<br>

2. `Prepare_data.py` <br>
수집된 데이터를 적절한 형식으로 만들어주고 병합.<br>
data_source.txt에서 수집하고자하는 지점을 추가하는경우, 코드 내에서 튜닝(수위->해발표고)을해줘야 함.<br>

3. `EDA.ipynb` <br>
수집된 데이터들을 이용하여 각종 EDA 및 feature engineering.<br>

4. `Modeling.ipynb` <br>
선행시간별로 잠수교의 수위를 예측하여 실제 수위와 비교.<br>

### 4. Result <br>
선행시간별 2023년 잠수교 수위 예측 결과<br>
표 넣기

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
