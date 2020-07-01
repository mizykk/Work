# 데이터 처리
import re   # 정규표현식
import numpy as np   # 넘파이
import pandas as pd   # 판다스 
import itertools   # 리스트 해제
import time

# DataBase
import pymysql
from sqlalchemy import create_engine

# Bigquery
from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1

# 경고 안뜨게
import warnings   
warnings.filterwarnings(action='ignore')
# 최대 출력 행 늘리기
pd.set_option('display.max_rows', 500)
# 최대 출력 열 늘리기
pd.set_option('display.max_columns', 500)

class mg:
    # 빅쿼리에서 데이터 가져오기
    def get_bq(query):
        credintails_path = ### 입력 ###
        project_id = ### 입력 ###
        credentials = service_account.Credentials.from_service_account_file(credintails_path)
        bqclient = bigquery.Client(credentials=credentials, project=project_id)
        bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient(credentials=credentials)

        start = time.time()
        query_job = bqclient.query(query)
        results = query_job.result()
        result_df = results.to_dataframe()
        # engine_upload(host_name='ds', db_name = 'mycelebs_ga', table_name= 'maimovie_keytalk', upload_df=result_df)
        duration_time = round(time.time() - start)

        print(f'- - - - - 완료 ({duration_time}초 / {round(duration_time/60, 2)}) - - - - -')
        return result_df

    # DB에서 데이터 가져오기
    def get_db(query, db_name):
        host_url = ### 입력 ###
        user_nm = ### 입력 ###
        passwd = ### 입력 ###
        port_num = 3306

        engine = create_engine(f'mysql+pymysql://{user_nm}:{passwd}@{host_url}:{port_num}/{db_name}?charset=utf8')
        engine_conn = engine.connect()

        data = pd.read_sql(query, engine_conn)

        engine_conn.close()
        print('- - - - - 완료 - - - - -')
        return data
    
    # hit_path 만들기
    def mk_hits(self, df):
        df['hits'] = np.where(df['hits.type']=='[PAGE]', 
                              df['hits.type'] + df['hits.page.pagePath'], 
                              df['hits.type'] + df['hits.page.pagePath'] + '+' + df['hits.eventInfo.eventCategory'] + '/' + df['hits.eventInfo.eventAction'] + '/' + df['hits.eventInfo.eventLabel'])

        # hits에서 띄어쓰기 없애기
        df['hits'] = df['hits'].str.replace(' ', '_')
        
        # hits_path 만들기
        df_hits = df.sort_values(['session_key', 'mcd_pk', 'date']).reset_index(drop = True)
        dh = df_hits.groupby(['session_key'])['hits'].apply(lambda x: ' > '.join(x))
        path = pd.DataFrame({'session_key': dh.index, 'path': dh.values})
        return path
    
    # 중복 경로 제거(reduce duplicate path)
    def rdp(self, df):
        i = 1
        # 경로 나누기
        list_temp = df.split(' > ')[0]
    
        # 뒤의 경로가 앞의 경로와 일치하면 뒷 경로 제거
        while i < len(df.split(' > ')):
            if df.split(' > ')[i] != df.split(' > ')[i-1]:
                list_temp = list_temp + ' > ' + df.split(' > ')[i]
            i += 1
        return list_temp
    
    # hits 정제
    def clean_hits(self, df):
        # tutorial 중복인거 제거
        for i in range(0, 3):
            df['path'] = df['path'].str.replace('\[PAGE\]/tutorial_02 > \[PAGE\]/tutorial_01', '[PAGE]/tutorial_02')
            df['path'] = df['path'].str.replace('\[PAGE\]/tutorial_01 > \[PAGE\]/tutorial_01', '[PAGE]/tutorial_01')
        
        # 중복 경로 정제
        df['path'] = df['path'].apply(lambda x: self.rdp(x))

        return path