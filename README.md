# Waterlevel prediction (last update 2023.10.23)

## 2023년 잠수교 수위 예측 (1월 ~ 9월) <br>



[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBae-ChangHyun%2FWaterlevel-predict&count_bg=%23113CD5&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) <br>
<img alt="GitHub forks" src="https://img.shields.io/github/forks/Bae-ChangHyun/Waterlevel-predict">

개발기간: <br>
`개인`(2022.05 ~ 2023.05) <br>

### 1. Subject <br>
대한민국 강원도의 산불 발생 확률(0~1)을 기상, 지형, 인적 데이터를 이용하여 예측하는 프로젝트.<br>
기상 데이터는 tabular 데이터로, 지형과 인적데이터는 image 데이터로 구성하여,<br> 멀티모달 학습방식을 사용하여 모델 학습.<br>

- 기상데이터: 기온,습도,풍속,강수량<br>
- 지형데이터: 고도, 경사도, NDVI<br>
- 인적데이터: 인구밀도, 토지이용도<br>

프로젝트 회고 -> [블로그](https://changsroad.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%82%B0%EB%B6%88%20%EB%B0%9C%EC%83%9D%20%EC%98%88%EC%B8%A1)

### 2. Installation <br>

아래 구글드라이브에서 두 파일을 다운로드 후, [wiki](https://github.com/Bae-ChangHyun/Forestfire-predict/wiki/Simple-Code-discription)에 기재되어 있는 사전준비를 미리 해놔야 코드가 오류없이 돌아갑니다.<br>
또한 설정된 파일 경로와 파일명을 임의로 바꾸면 안됩니다. <br>
[raw파일다운로드](https://drive.google.com/file/d/1Kew7kQTDRqo_X_-T-rW06XjGvHvlBEMm/view?usp=drive_link) / 
[asos파일다운로드](https://drive.google.com/file/d/1KfERjVehpwHckMcY6gKZHB8tRyKIegVM/view?usp=drive_link)  <br>

! 데이터의 용량이 크기 때문에 작업 디렉토리를 용량이 넓은 드라이브에 설정 하는 것을 추천합니다

### 3. Run <br>
`train_model.py`(데이터 수집 및 모델 학습)의 총 실행시간은 대략 2일정도 걸립니다. <br>
단, 멈췄다가 재시작할시 이전 중단지점부터 다시 시작하기 때문에 멈췄다가 다시 실행하여도 상관없습니다. <br>

`train_model.py`의 경우 실행후, 아무것도 입력할 필요없으며, <br>
`test_model.py`의 경우 실행 후, prompt에 안내되는 형식에 따라 input 숫자를 입력하면 됩니다. <br>
(과거시점의 경우 입력되는 날짜/시간의 산불발생확률맵을 생성, <br> 미래시점(오늘+2일내)의 경우 입력되는 날짜 이후 1시간30분, 2시간 30분, 3시간30분 뒤의 산불발생확률맵을 생) <br>

```python
pip install -r requirements.txt
python train_model.py
python test_model.py
```
### 4. Result <br>
[2022.03.04 12:00 강원도 영월 산불]-(좌측:국가산불위험예보시스템 / 우측: 프로젝트산출물) <br>
<img src="https://github.com/Bae-ChangHyun/Forestfire-predict--multimodal/assets/48899047/a5336b36-6114-4da3-9316-51624fac2c19.png"  width="600" height="300"/>


<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/qgis-589632?style=for-the-badge&logo=qgis&logoColor=white">
  <img src="https://img.shields.io/badge/gdal-5CAE58?style=for-the-badge&logo=gdal&logoColor=white">
  <br>
</div>
