# Waterlevel prediction
2023년 홍수기 잠수교 수위 예측

## [Collect_data.py]

- Origin 데이터수집- api를 이용한 크롤링 방식

  <b>유의사항</b> <br>
  -> 미리 한강홍수통제소, 바다누리해양정보서비스의 API키를 발급받아야 함.<br>
  -> 오타 입력시 경고없이 종료됨.<br>
  -> 모두 10분간격의 데이터로 수집됨.<br>
  -> 현재 디렉토리 하위에 data라는 폴더를 생성하고 아래 폴더명으로 파일 자 생성됨.<br>
  -> 년,월별로 파일이 개별 생성 이후 다음 Preprocesisng_data.py를 이용하여 병합해야함.<br>
  -> 현재 년, 월 이후를 입력시 오류 발생(추후 입력불가하게 수정예정)<br>
  -> 다른 지점의 데이터를 얻기위해서는 py내부 get_info함수에 동일 형식으로 추가해주면 됨.<br>
  
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

## [Preprocessing_data.py] <br>

- Origin 데이터 병합 <br>

<b>유의사항</b> <br>
-> 미리 Collect_data.py를 이용하여 데이터를 수집해야함.(경로 변경x) <br>
-> 오타 입력시 경고없이 종료됨. <br>
-> 기본 제공 지점 외 다른 지점을 추가로 수집했을 경우 def preprocessing에서 수위->해발표고 값으로 튜닝해줘야 함.  <br>
-> 기본적으로 년,월,카테고리로 나눠있는 데이터들을 병합하는 용도. <br>
