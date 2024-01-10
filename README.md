# Waterlevel prediction (last update 2023.12.15)

## 한강 수위 예측 <br>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBae-ChangHyun%2FWaterlevel-predict&count_bg=%23113CD5&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 
<img alt="GitHub forks" src="https://img.shields.io/github/forks/Bae-ChangHyun/Waterlevel-predict">

프로젝트 기간: <br>
`개인`(2022.05 ~ 2023.05) <br>

<a href="https://changsroad.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%88%98%EC%9C%84%20%EC%98%88%EC%B8%A1"><img src="https://img.shields.io/badge/주제1-333333?style=%20for-the-badge&logo=tistory&logoColor=%23333333&color=%23fc4e42&link=[https%3A%2F%2Fchangsroad.tistory.com%2F](https://changsroad.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%88%98%EC%9C%84%20%EC%98%88%EC%B8%A1)"/></a> 
<a href="https://www.notion.so/55301e5d1c8f4c08b78db12de2e16994?pvs=4"><img src="https://img.shields.io/badge/%EC%A3%BC%EC%A0%9C2-3776AB?logo=notion&logoColor=%23000000&color=%23FFFFFF&link=https%3A%2F%2Fwww.notion.so%2F55301e5d1c8f4c08b78db12de2e16994%3Fpvs%3D4"/></a>
<a href="https://github.com/Bae-ChangHyun/Waterlevel-predict/wiki"><img src="https://img.shields.io/badge/wiki-3776AB?logo=wikipedia&logoColor=%23000000&color=%23FFFFFF&link=https%3A%2F%2Fgithub.com%2FBae-ChangHyun%2FWaterlevel-predict%2Fwiki"/></a>

### 1. Subject <br>
1. `Subject 1` <br>
  잠수교,한강대교,행주대교,청담대교 2023년 1~9월 수위(해발표고)를 선행시간 10분에 예측<br>
2. `Subject 2` <br>
  잠수교의 2023년 1~9월 수위(해발표고)를 선행시간에 따라 예측<br>

### 2. File <br>
1. `Collect_data.py`<br>
= 사용자 정의에 맞게 데이터를 수집할 수 있도록 자동화한 파일. <br>
api 크롤링을 통해 한강홍수통제소, 바다누리해양정보서비스에서 데이터를 수집. <br>
data_source.txt에 적혀있는 대교와 댐 데이터를 수집함.<br>
`/code` 에 `.env` 파일을 생성하고 미리 api key를 입력해줘야 함.(노션 참조)<br>

2. `Prepare_data.py` <br>
= 수집된 데이터의 기본적인 병합 및 전처리.<br>
기본 지점 외 수집하고자하는 지점을 추가한경우, 코드 내에서 수위->해발표고로 변환해주는 작업을 따로 진행해줘야 함.(노션 참조)<br>

3. `EDA.ipynb` <br>
= 데이터 EDA, 전처리(이상치,결측치) 및 Feature Engineering 진행 <br>

4. `hangang_predict.ipynb` <br>
= [subject 1]에 해당하는 모델링 및 결과 확인. <br>
잠수교, 한강대교, 청담대교, 행주대교의 선행시간 10분에 예측.<br>

4. `leadtime_predict.ipynb`  <br>
= [subject 2]에 해당하는 모델링 및 결과 확인. <br>
잠수교 수위를 다양한 선행시간에 따라 예측 및 분석.<br> 

### 3. Result <br>
[subject 1]: 4개의 대교의 수위를 선행시간 10분에 예측하여 아래와 같은 오차를 기록하였다.<br>
`청담대교`: 1.119 / `잠수교`: 0.9163 / `한강대교`:1.022 / `행주대교`:0.9889 <br>
[subject 2]: <br>
`leadtime(10)`:1.298 / `leadtime(60)`:3.608 / `leadtime(180)`:16.262 <br>
`leadtime(540)`:18.486 / `leadtime(720)`:22.587 / `leadtime(1440)`:40.086 <br>

자세한 결과는 노션참조

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
