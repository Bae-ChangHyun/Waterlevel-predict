import os
from glob import glob

import numpy as np
import pandas as pd

import requests
import calendar
import time

#! 업데이트 해야 할 내용
#! 현재날짜와 현재월 불러오고 그거 이상으로는 입력안되도록 변경하기
#! 입력형식 맞지 않게 입력해도 다시 입력하게 바꾸기


def get_info(source):

    if (source == 'bridge'):
        url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/waterlevel/list/10M/"
        table = {
            '서울시(청담대교)': 1018662,
            '서울시(잠수교)': 1018680,
            '서울시(한강대교)': 1018683,
            '서울시(행주대교)': 1019630,
            '서울시(광진교)': 1018640,
            '남양주시(팔당대교)': 1018610,
            '서울시(중랑교)': 1018675
        }
    elif (source == 'dam'):
        url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/dam/list/10M/"
        table = {
            '팔당댐': 1017310
        }
    elif (source == 'rf'):
        url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/rainfall/list/10M/"
        table = {
            '서울시(대곡교)': 10184100,
            '남양주시(진관교)': 10184110,
            '서울시(송정동)': 10184140
        }
    else:
        url = f"http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={SERVICE_KEY2}"
        table = {
            '강화대교': 'DT_0032'
        }

    return url, table


def collect_data(start, end, source):

    # 입력받은 데이터 수집 기간(년,월로 나눠줌)
    start_year, end_year = int(start[:-2]), int(end[:-2])
    start_month, end_month = int(start[-2:]), int(end[-2:])

    # 크롤링 할 url과 지점 코드를 가져옴.
    origin_url, table = get_info(source)

    for name, code in table.items():
        print(f"{name} Crawling start ###################")
        os.makedirs(f'{script_dir}/../data/{source}/{name}',
                    exist_ok=True)  # 하위 폴더가 없을시 생성
        for year in range(start_year, end_year+1):    # 시작년도 ~ 마지막년도
            for month in range(start_month, end_month+1):  # 시작월 ~ 마지막 월

                # 해당 년,월의 마지막 날짜를 구해줌(ex.2월은 28일)
                weekday, end = calendar.monthrange(year, month)

                # [한강 홍수 통제소]-대교,댐,강수량 데이터
                # 10분 간격의 데이터, 시간별로 기록되어 있음
                # 시간별 데이터->월별 데이터로 변환
                if (source != 'tide'):
                    start_date, end_date = f"{year}{month:02}010000", f"{year}{month:02}{end:02}2350"
                    url = origin_url+f"{code}/{start_date}/{end_date}.json"
                    response = requests.get(url, verify=False)
                    df = pd.DataFrame(response.json()['content'])

                # [바다누리 해양정보 서비스] 조위 데이터
                # 1분 간격의 데이터, 일별로 기록되어 있음
                # 1분 간격, 일별 데이터 -> 10분 간격, 월별 데이터로 변환
                else:
                    df_month = []
                    for day in range(1, end+1):
                        start_date = f"{year}{month:02}{day:02}"
                        url = origin_url + \
                            f"&ObsCode={code}&Date={start_date}&ResultType=json"
                        response = requests.get(url, verify=False)
                        try:
                            df = pd.DataFrame(
                                response.json()['result']['data'])
                            df = df.set_index('record_time', drop=True)
                            df.index = pd.to_datetime(df.index)
                            df['tide_level'] = df['tide_level'].astype('int')
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
                df.to_csv(
                    f"{script_dir}/../data/{source}/{name}/{year}{month:02}_{name}.csv", index=False)
                time.sleep(3)
            print(f"{year} end ")
        print(f"{name} Crawling end ###################")


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로를 가져옴
    SERVICE_KEY = input("발급받은 한강홍수통제소 API를 입력하세요.")
    SERVICE_KEY2 = input("발급받은 바다누리통제소 API를 입력하세요.")

    while True:
        source = input(
            "bridge / dam / rf / tide 중 하나를 입력하세요.(종료하려면 아무 키나 입력하세요): ")
        if source not in ['bridge', 'dam', 'rf', 'tide']:
            break
        start = input("시작일을 입력하세요(Ex. 202309)")
        end = input("종료일를 입력하세요(Ex. 202311)")
        collect_data(start, end, source)
        print("요청하신 데이터 수집이 완료되었습니다.")
