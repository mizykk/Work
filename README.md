# Work

데이터를 올릴 수는 없지만.. 코드는 정리해서 올리는 곳

[🍎](https://github.com/mizykk/Work/blob/master/Hit_path.ipynb) Hit Path 정제. 
[🍊](https://github.com/mizykk/Work/blob/master/URL_Encoding.ipynb) URL Encoding. 
[🍋](https://github.com/mizykk/Work/blob/master/%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%87%E1%85%A9%E1%86%A8%E1%84%8C%E1%85%A6%E1%84%80%E1%85%A5%20%26%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%87%E1%85%A9%E1%86%A8%E1%84%80%E1%85%A1%E1%86%B9%20%E1%84%8E%E1%85%A1%E1%86%BD%E1%84%80%E1%85%B5.ipynb) 중복제거 & 중복값 찾기. 

---  

### 🐰 python 🐰
- head() : 상위 n개 값만 보이기
- tail() : 하위 n개 값만 보이기
- sample() : 랜덤으로 n개 값만 보이기
- strip() : 문자열 양쪽 공백 제거하기
- split() : 문자열 나누기
- replace() : 문자열 변경하기
- append() : 리스트에 값 추가하기
- lambda

### 🐼 Pandas 🐼
import pandas as pd
- read_csv() : csv파일 불러오기
- read_excel() : 엑셀(xlsx)파일 불러오기
- dtypes : 데이터 타입 확인하기
- notnull() : 결측값 아닌 것만 보여주기
- reset_index() : 인덱스 초기화
- merge() : 데이터프레임 합치기
- DataFrame() : 데이터프레임 만들기
- fillna() : 결측값 채우기
- pivot_table() 
- apply() : 함수 한번에 적용하기
- drop_duplicates() : 중복제거하기
- to_csv() : csv로 내보내기
- to_excel() : 엑셀(xlsx)파일로 내보내기

### 🦊 re 🦊
- re.compile()
- re.sub() : 문자열 변경하기

### 🦋 urllib 🦋
from urllib import parse
- parse.urlparse() : Url parsing
- parse.parse_qs() : query를 파싱해서 딕셔너리로 반환
- parse.parse_qsl() : query를 파싱해서 리스트로 반환
- parse.urlencode() : Encoding


### 🐹 And more.. 🐹
import warnings  
warnings.filterwarnings(action='ignore') : 경고 안보이게
