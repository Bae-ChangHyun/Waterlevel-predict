import os
from glob import glob

import numpy as np
import pandas as pd

import requests
import calendar
import time
from dotenv import load_dotenv

#! 업데이트 해야 할 내용
#! 현재날짜와 현재월 불러오고 그거 이상으로는 입력안되도록 변경하기
#! 입력형식 맞지 않게 입력해도 다시 입력하게 바꾸기

# 파일에서 데이터를 읽어오는 함수
def load_table_from_file(filename, source):
    table = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if(len(parts)<1):continue
            file_source = parts[0][:-1]
            if file_source == source:
                key = " ".join(parts[1:-1])
                value=parts[-1]
                #value = int(parts[-1])
                table[key] = value
    return table


def get_info(source):
    table = load_table_from_file("data_source.txt", source)
    
    if source == 'bridge':url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/waterlevel/list/10M/"
    elif source == 'dam':url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/dam/list/10M/"
    elif source == 'rf':url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/rainfall/list/10M/"
    else:url = f"http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={SERVICE_KEY2}"
        
    return url, table

def collect_data(start, end, source):

    # 입력받은 데이터 수집 기간(년,월로 나눠줌)
    start_year, end_year = int(start[:-2]), int(end[:-2])
    start_month, end_month = int(start[-2:]), 12

    # 크롤링 할 url과 지점 코드를 가져옴.
    origin_url, table = get_info(source)

    for name, code in table.items():
        print(f"{name} Crawling start ###################")
        os.makedirs(f'{script_dir}/../data/{source}/{name}',exist_ok=True)  # 하위 폴더가 없을시 생성
        for year in range(start_year, end_year+1):    # 시작년도 ~ 마지막년도
            # 마지막년을 제외하고는 모두 12월까지. 
            if(year==end_year):end_month = int(end[-2:])
            else: end_month=12
            for month in range(start_month, end_month+1):  # 시작월 ~ 마지막 월
                # 해당 년,월의 마지막 날짜를 구해줌(ex.2월은 28일)
                weekday, ends = calendar.monthrange(year, month)

                # [한강 홍수 통제소]-대교,댐,강수량 데이터
                # 10분 간격의 데이터, 시간별로 기록되어 있음
                # 시간별 데이터->월별 데이터로 변환
                if (source != 'tide'):
                    start_date, end_date = f"{year}{month:02}010000", f"{year}{month:02}{ends:02}2350"
                    url = origin_url+f"{code}/{start_date}/{end_date}.json"
                    response = requests.get(url, verify=False)
                    df = pd.DataFrame(response.json()['content'])

                # [바다누리 해양정보 서비스] 조위 데이터
                # 1분 간격의 데이터, 일별로 기록되어 있음
                # 1분 간격, 일별 데이터 -> 10분 간격, 월별 데이터로 변환
                else:
                    df_month = []
                    for day in range(1, ends+1):
                        start_date = f"{year}{month:02}{day:02}"
                        url = origin_url + f"&ObsCode={code}&Date={start_date}&ResultType=json"
                        response = requests.get(url, verify=False)
                        try:
                            df = pd.DataFrame(response.json()['result']['data'])
                            df = df.set_index('record_time', drop=True)
                            df.index = pd.to_datetime(df.index)
                            df['tide_level'] = df['tide_level'].astype('float')
                            # 1분간격의 데이터를 10분간격의 데이터로 변환
                            df = df.resample('10T').mean()
                            # 일별 데이터를 하나의 리스트로 모음
                            df_month.append(df)
                        except:
                            pass
                    try:
                        # 일별 데이터를 월별 데이터로 변환
                        df = pd.concat(df_month, axis=0)
                    except:
                        #! 추후 오늘 날짜 이후로 안되도록 변경하면 이 부분은 제거해도 됨
                        print("존재하지 않는 일자입니다.")
                        break
                    df['record_time'] = df.index
                df.to_csv(f"{script_dir}/../data/{source}/{name}/{year}{month:02}_{name}.csv", index=False)
                time.sleep(3)
            print(f"{year} end ")
        print(f"{name} Crawling end ###################")


if __name__ == "__main__":
    load_dotenv()
    SERVICE_KEY = os.getenv("SERVICE_KEY")
    if(SERVICE_KEY==None):
        print("발급받은 한강홍수통제소 API를 세팅해주세요.")
        exit()
    SERVICE_KEY2 = os.getenv("SERVICE_KEY2")
    if(SERVICE_KEY2==None):
        print("발급받은 바다누리통제소 API를 세팅해주세요")
        exit()
    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로를 가져옴

    while True:
        source = input("bridge / dam / rf / tide 중 하나를 입력하세요.(종료하려면 아무 키나 입력하세요): ")
        if source not in ['bridge', 'dam', 'rf', 'tide']:break
        start = input("시작일을 입력하세요(Ex. 202309): ")
        end = input("종료일를 입력하세요(Ex. 202311): ")
        collect_data(start, end, source)
        print("요청하신 데이터 수집이 완료되었습니다.")
