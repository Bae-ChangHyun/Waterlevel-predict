import numpy as np
import pandas as pd
import os
from glob import glob
from functools import reduce
import warnings

# dtype warning 무시
warnings.filterwarnings("ignore", category=pd.errors.DtypeWarning)

# py파일로 실행할 경우, 상대경로를 인식하지 못할 수도 있기 때문에,
# 반드시 script_dir = os.path.dirname(__file__)를 통해 현재 py파일의 경로를 인식시켜주고
# 파일경로 앞에 script_dir, / 를 추가해줘야 함.

# 크롤링한 데이터 로드
def load_data(source):

    # 한강에 있는 대교들의 수위 및 유량------------------
    if (source == 'bridge'):
        jamsu = sorted(glob(f"{script_dir}/../data/bridge/서울시(잠수교)/*.csv"))
        cheongdam = sorted(glob(f"{script_dir}/../data/bridge/서울시(청담대교)/*.csv"))
        haengju = sorted(glob(f"{script_dir}/../data/bridge/서울시(행주대교)/*.csv"))
        hangang = sorted(glob(f"{script_dir}/../data/bridge/서울시(한강대교)/*.csv"))
        gwangin = sorted(glob(f"{script_dir}/../data/bridge/서울시(광진교)/*.csv"))
        paldang = sorted(glob(f"{script_dir}/../data/bridge/남양주시(팔당대교)/*.csv"))
        jungnang = sorted(glob(f"{script_dir}/../data/bridge/서울시(중랑교)/*.csv"))
        jeollyuri = sorted(glob(f"{script_dir}/../data/bridge/김포시(전류리)/*.csv"))

        data_list = {"jamsu": jamsu, "cheongdam": cheongdam, "haengju": haengju,
                     "hangang": hangang, "gwangin": gwangin, "paldang": paldang, 
                     "jungnang": jungnang,"jeollyuri":jeollyuri}
        
        drop_cols = ['wlobscd', 'links']

    # 팔당댐 관련 변수들들 ----------------------------------------
    elif (source == 'dam'):
        pd_dam = sorted(glob(f"{script_dir}/../data/dam/팔당댐/*.csv"))

        data_list = {'pd_dam': pd_dam}
        drop_cols = ['dmobscd', 'links']

    # 강화대교 조위-----------------------------------
    elif (source == 'tide'):
        tide_lv = sorted(glob(f"{script_dir}/../data/tide/강화대교/*.csv"))

        data_list = {'tide_lv': tide_lv}
        drop_cols = []
        
    # 강수량 ------------------------------------------
    elif (source == 'rf'):
        zingwan = sorted(glob(f"{script_dir}/../data/rf/남양주시(진관교)/*.csv"))
        daegog = sorted(glob(f"{script_dir}/../data/rf/서울시(대곡교)/*.csv"))
        songjeong = sorted(glob(f"{script_dir}/../data/rf/서울시(송정동)/*.csv"))

        data_list = {'zingwan': zingwan,'daegog': daegog, 'songjeong': songjeong}
        drop_cols = ['rfobscd', 'links']

    return data_list, drop_cols


def preprocessing(source, data_storage):

    # 수위값을 해발표고 값으로 변환
    # 한강홍수통제소에서 수위<->해발표고의 차이를 비교하여 개별 튜닝해야 함.
    if (source == 'bridge'):
        calc = {"jamsu": -6.8, "cheongdam": 174.7, "haengju": 80.3,
                "hangang": 207, "gwangin": 528, "paldang": 557.0,
                "jungnang": 917,"jeollyuri":-10}

        for i in data_storage:
            data_storage[i]['wl'] = data_storage[i]['wl'].replace(' ', '0')
            data_storage[i]['wl'] = data_storage[i]['wl'].astype('float')
            data_storage[i]['wl'] = data_storage[i]['wl']*100 + calc[i]

            data_storage[i].columns = ['ymdhm', 'wl_'+i, 'fw_'+i]

    elif (source == 'rf'):
        for i in data_storage:
            data_storage[i].columns = ['ymdhm', 'rf_'+i]

    return data_storage


def save_data(source, data_storage):

    # 데이터들을 병합하고 저장 총 4개(bridge, dam, rf, tide) 데이터가 생성됨
    data = [data_storage[i] for i in data_storage]
    data = reduce(lambda left, right: pd.merge(left, right, on='ymdhm'), data)
    data.replace(" ", np.nan, inplace=True)
    data = data.sort_values(by='ymdhm', ascending=True)
    data = data.drop_duplicates(subset='ymdhm', keep='first')
    data.to_csv(f'{script_dir}/../data/{source}/full_{source}.csv')

    return data


def merge_data(source):

    data, drop_cols = load_data(source)
    # 각 대교의 이름과 데이터들이 담겨있는 리스트
    data_storage = dict()

    for river in data.keys():
        print("#"*20)
        print(f"{river} data Merge Start")
        tmp_df = []
        # 년,월별로 나뉘어진 데이터들을 병합
        for file in data[river]:
            tmp = pd.read_csv(file)
            tmp_df.append(tmp)
        full_df = pd.concat(tmp_df, axis=0)
        full_df.reset_index(drop=True, inplace=True)
        full_df.drop(drop_cols, axis=1, inplace=True)
        
        if source != 'tide':
            full_df['ymdhm'] = pd.to_datetime(full_df['ymdhm'], format='%Y%m%d%H%M')
        # 조위 데이터의 경우 형식이 달라 개별 처리
        else:
            full_df['record_time'] = pd.to_datetime(full_df['record_time'], format='%Y-%m-%d %H:%M:%S')
            full_df.columns = ['tide_level','ymdhm' ]
            
        full_df = full_df.sort_values(by='ymdhm')
        full_df = full_df.reset_index(drop=True)
        data_storage[river] = full_df
        print(f"{river} data Merge complete")
    return data_storage


def check_data():
    prev = glob(os.path.join(script_dir, "../data/full_data.csv"))
    if (prev != []):
        return 1
    else:
        return 0


def finalize_data():
    answer = int(input("파일을 병합하려면 1, 아니면 0을 입력하세요. "))
    if (answer == 1):
        if (check_data() == 0):
            # 각 source별 병합된 파일 가져옴.(dam,bridge,rf,tide)
            dam_data = pd.read_csv(f"{script_dir}/../data/dam/full_dam.csv", index_col=0)
            bridge_data = pd.read_csv(f"{script_dir}/../data/bridge/full_bridge.csv", index_col=0)
            rf_data = pd.read_csv(f"{script_dir}/../data/rf/full_rf.csv", index_col=0)
            tide_data = pd.read_csv(f"{script_dir}/../data/tide/full_tide.csv", index_col=0)
            # 데이터 전체 병합
            final_df = [bridge_data, dam_data, rf_data, tide_data]
            for df in final_df:df['ymdhm'] = pd.to_datetime(df['ymdhm'])
            final_data = reduce(lambda left, right: pd.merge(left, right, on='ymdhm', how='outer'), final_df)
            final_data = final_data[:-1]
            # 데이터 기본 전처리
            final_data=final_data.replace('##########',np.nan)
            final_data=final_data.replace(' ',np.nan)
            #final_data.set_index(final_data['ymdhm'],drop=True,inplace=True)
            final_data.to_csv(f"{script_dir}/../data/full_data.csv",index=False)
        else: 
            print("이미 데이터가 존재합니다.")
            final_data = pd.read_csv(f"{script_dir}/../data/full_data.csv", index_col=0)
    else:
        print("작업을 종료합니다.")
    return 0


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로를 가져옴
    while True:
        source = input(
            "bridge / dam / rf / tide 중 하나를 입력하세요.(종료하려면 아무 키나 입력하세요): ")
        if source not in ['bridge', 'dam', 'rf', 'tide']:
            break
        if (check_data() == 0):
            data_storage = merge_data(source)
            data_storage = preprocessing(source, data_storage)
            data = save_data(source, data_storage)
        else:
            break
        print("요청하신 데이터 전처리가 완료되었습니다.")
    finalize_data()
print("데이터 저장이 완료되었습니다.")
