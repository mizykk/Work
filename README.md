# Work

데이터를 올릴 수는 없지만.. 코드는 정리해서 올리는 곳

[🍏](https://github.com/mizykk/Work/blob/master/Convert_Hex_color_to_Color_name.ipynb) Convert_Hex_color_to_Color_name : Hex color를 색상명으로 변경  
[🍎](https://github.com/mizykk/Work/blob/master/Find_duplicates.ipynb) Find_duplicates : 중복제거 & 중복찾기   
[🍊](https://github.com/mizykk/Work/blob/master/Find_values_in_nested_dictionary.ipynb) Find_values_in_nested_dictionary : 중첩 딕셔너리에서 값 찾기   
[🍋](https://github.com/mizykk/Work/blob/master/Find_words_in_sentences.ipynb) Find_words_in_sentences : 문장 속에서 단어 찾기   
[🍉](https://github.com/mizykk/Work/blob/master/Getting_RGB_values_from_image.ipynb) Getting_RGB_values_from_image : 이미지에서 RGB 추출하기(화장품 색상)  
[🍇](https://github.com/mizykk/Work/blob/master/Hit_path.ipynb) Hit_Path : GA hitsPath 정제     
[🍓](https://github.com/mizykk/Work/blob/master/Movie_check.ipynb) Movie_check : 영화 개봉일이 2개월 이후인지 & 성인영화인지 판단  
[🍒](https://github.com/mizykk/Work/blob/master/URL_Encoding.ipynb) URL_Encoding : URL 인코딩     
[🍑](https://github.com/mizykk/Work/blob/master/Word_Cloud.ipynb) Word_Cloud : 워드클라우드   

---   
   
### 🐰 python 🐰  
`len()` : 길이     
`lower()` : 소문자로  
`upper()` : 대문자로
`strip()` : 문자열 양쪽 공백 제거하기    
`split()` : 문자열 나누기    
`replace()` : 문자열 변경하기     
`append()` : 리스트에 값 추가하기   
`lambda`    
`map`  
`apply`  
   
### 🐼 Pandas 🐼   
`import pandas as pd`  
`pd.read_csv()` : csv파일 불러오기  
`pd.read_excel()` : 엑셀(xlsx)파일 불러오기  
`df.dtypes` : 데이터 타입 확인하기  
`.head()` : 상위 n개 값만 보이기    
`.tail()` : 하위 n개 값만 보이기    
`.sample()` : 랜덤으로 n개 값만 보이기 
`.unique()` : 고유값  
`pd.isnull()` : 결측값이 있는 것  
`pd.notnull()` : 결측값 아닌 것만 보여주기  
`df.fillna()` : 결측값 채우기    
`pd.reset_index()` : 인덱스 초기화  
`pd.merge(df1, df2, by = , how = )` : 데이터프레임 합치기  
`pd.concat([df1, df2], axis = )` : 데이터프레임 합치기  
`pd.DataFrame()` : 데이터프레임 만들기  
`pd.pivot_table()` : 피봇테이블   
`df.apply()` : 함수 한번에 적용하기    
`pd.drop_duplicates(['col'], keep = )` : 중복제거하기    
`.isin()` : A가 B안에 들어있는지    
`df.to_csv()` : csv로 내보내기  
`df.to_excel()` : 엑셀(xlsx)파일로 내보내기  

### 🦁 re 🦁     
`import re`   
`re.compile('exp')`  
`re.sub('after', 'before')` : 문자열 변경하기 
`re.findall()` : 컴파일 된 정규식과 일치하는 문자를 찾아서 리스트로 반환     

### 🦋 urllib 🦋  
`from urllib import parse`  
`parse.urlparse()` : Url parsing  
`parse.parse_qs()` : query를 파싱해서 딕셔너리로 반환  
`parse.parse_qsl()` : query를 파싱해서 리스트로 반환  
`parse.urlencode()` : Encoding  
  
### 🐹 Datetime 🐹  
`from datetime import datetime`
`datetime.datetime.now()` : 현재시각  
`datetime.date()` : 날짜만 출력  
`datetime.time()` : 시간만 출력   
`datetime.strftime()` : datetime을 문자열로 변환해준다.     
`datetime.strptime(date_string, format)` : 문자열을 datetime으로 변환해준다.    
  
### 🦊 Crawling 🦊  
`import requests
from bs4 import BeautifulSoup`
`rq = requests.get(url)` : Get request    
`html = rq.text` : HTML 가져오기  
`bs = BeautifulSoup(html, 'html.parser')` : HTML Parsing     
`bs.find(tag).text` : tag에 해당하는 문자 가져오기  
`bs.find('div', class_ = '클래스명')` : Class로 찾기  
`bs.find('div', id = 'id명')` : Id로 찾기  
    
### 🐮 Connect with Database 🐮  
데이터베이스에서 데이터 가져오기    
`import pymysql  
from sqlalchemy import create_engine  
   
engine = create_engine(f'mysql+pymysql://{user_nm}:{passwd}@{host_url}:{port_num}/{db_name}?charset=utf8')  
engine_conn = engine.connect()  
   
data = pd.read_sql("""  
    Query  
    """, engine_conn)  
   
engine_conn.close()`

데이터베이스에 테이블 업로드  
`engine = create_engine(f'mysql+pymysql://{user_nm}:{passwd}@{host_url}:{port_num}/{db_name}?charset=utf8')  
engine_conn = engine.connect()  
data.to_sql(table_name, engine_conn, if_exists='replace', index=None)  
engine_conn.close()  
engine.dispose()`
if_exist = {'replace', 'append', 'fail')   


### 🐹 And more.. 🐹   
경고 안 나타나게     
`import warnings`       
`warnings.filterwarnings(action='ignore')`  
     
    
멀티프로세싱  
`if __name__=='__main__':  
    pool = Pool(processes=12)  
    result = pool.map(get_color_name, range(0, len(data)))`  


문자열을 딕셔너리로    
`from ast import literal_eval`   
`literal_eval()`


URL로 이미지 불러오기   
`from PIL import Image
from io import BytesIO
response = requests.get(data['palette'][i])  
img = Image.open(BytesIO(response.content))  
col = img.load()`    

토큰화 & Stopwords 제거  
`from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

def remove_stopwords(words):
    words = [w for w in words if w not in stopwords.words('english')]
    return words
    
text_to_word_sequence(x))`  
  
복수형을 단수로 만들기   
`from nltk.stem import WordNetLemmatizer 
lemm = WordNetLemmatizer()
emm.lemmatize()`
