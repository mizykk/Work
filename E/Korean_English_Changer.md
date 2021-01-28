
# 동의어사전 - 한글/영어 키보드 기준 변환

2021-01-28  
&nbsp;  
주어진 키워드를..
- 한글로 적혀진 것 > 키보드 기준 영어로  
- 영어로 적혀진 것 > 키보드 기준 한글로  

변환하는 작업을 하였다.  
유입되는 검색어 중에 한/영 전환이 필요한 키워드를 찾기 위한 것이다.


```python
import pandas as pd
import re
import warnings
warnings.filterwarnings(action='ignore')
```

파일불러오기


```python
sd = pd.read_excel('data.xlsx')
```

## 한글 → 영어로 변환

1. 자소분리  
사과 → ㅅㅏㄱㅘ


```python
from jamo import h2j, j2hcj

sd['자소분리'] = sd['keyword'].apply(lambda x: j2hcj(h2j(x)) if type(x) == str else x)
```

2. 한글-영문 키보드입력에 맞추어 변환


```python
keyboard = {'ㄱ':'r', 'ㄲ':'R', 'ㄴ':'s', 'ㄷ':'e', 'ㄸ':'E', 'ㄹ':'f', 'ㅁ':'a', 'ㅂ':'q', 'ㅃ':'Q', 'ㅅ':'t', 'ㅆ':'T',
           'ㅇ':'d', 'ㅈ':'w', 'ㅉ':'W', 'ㅊ':'c', 'ㅋ':'z', 'ㅌ':'x', 'ㅍ':'v', 'ㅎ':'g',
           'ㅏ':'k', 'ㅐ':'o', 'ㅑ':'i', 'ㅒ':'O', 'ㅓ':'j', 'ㅔ':'p', 'ㅕ':'u', 'ㅖ':'P', 'ㅗ':'h', 'ㅘ':'hk', 'ㅙ':'ho', 'ㅚ':'hl',
           'ㅛ':'y', 'ㅜ':'n', 'ㅝ':'nj', 'ㅞ':'np', 'ㅟ':'nl', 'ㅠ':'b',  'ㅡ':'m', 'ㅢ':'ml', 'ㅣ':'l',
           'ㄳ':'rt', 'ㄵ':'sw', 'ㄶ':'sg', 'ㄺ':'fr', 'ㄻ':'fa', 'ㄼ':'fq', 'ㄽ':'ft', 'ㄾ':'fx', 'ㄿ':'fv', 'ㅀ':'fg', 'ㅄ':'qt'}

def keng(kwd):
    return ''.join([keyboard[w] if w in keyboard else w for w in kwd])
```


```python
sd['keyword_Eng'] = sd['자소분리'].apply(lambda x: keng(x) if type(x) == str else x)
```

결과 예시


```python
sd[['keyword', '자소분리', 'keyword_Eng']].sample(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keyword</th>
      <th>자소분리</th>
      <th>keyword_Eng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>104231</th>
      <td>캘리포니아베이비</td>
      <td>ㅋㅐㄹㄹㅣㅍㅗㄴㅣㅇㅏㅂㅔㅇㅣㅂㅣ</td>
      <td>zofflvhsldkqpdlql</td>
    </tr>
    <tr>
      <th>7085</th>
      <td>직수정수기</td>
      <td>ㅈㅣㄱㅅㅜㅈㅓㅇㅅㅜㄱㅣ</td>
      <td>wlrtnwjdtnrl</td>
    </tr>
    <tr>
      <th>200099</th>
      <td>3학년권장도서</td>
      <td>3ㅎㅏㄱㄴㅕㄴㄱㅝㄴㅈㅏㅇㄷㅗㅅㅓ</td>
      <td>3gkrsusrnjswkdehtj</td>
    </tr>
  </tbody>
</table>
</div>



## 영어 → 한글로 변환

1. 영문-한글 키보드 딕셔너리 생성
    - 초성 : fst_kor
    - 중성 : mid_kor
    - 종성 : last_kor


```python
fst_kor = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ',
           'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ'}

mid_kor = {'k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ',
           'y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ',  'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ'}

last_kor = {'':'', 'r':'ㄱ', 'R':'ㄲ', 'rt':'ㄳ', 's':'ㄴ', 'sw':'ㄵ', 'sg':'ㄶ', 'e':'ㄷ', 
            'f':'ㄹ', 'fr':'ㄺ', 'fa':'ㄻ', 'fq':'ㄼ', 'ft':'ㄽ', 'fx':'ㄾ', 'fv':'ㄿ', 'fg':'ㅀ',
           'q':'ㅂ', 'qt':'ㅄ', 't':'ㅅ', 'T':'ㅆ', 'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ'}
```

2. 영문을 한글로 변환 & 한글 자모 결합


```python
#! pip install hangul-utils
from hangul_utils import join_jamos

def engkor(text):
    temp = ''
    i = 0
    while i < len(text):
        k2 = text[i:i+2]   # ㄻ ㅞ 같은 글자는 알파벳이 두개가 이어진 것으로 구성되어 있으므로 두 글자를 불러온다.
        # 초성은 해당하지 않아서 바로 중성에 있는지 검사한다.
        if k2 in mid_kor:   
            temp+=mid_kor[k2]
            j=2   # 있으면 다음 글자는 건너뛰어야해서 jump 2
        elif k2 in last_kor:
            temp+=last_kor[k2]
            j=2
        else:   # 연속된 두 알파벳이 중성/종성에 없었으므로 한 글자만 확인한다. 
            k1 = text[i]
            if k1 in fst_kor:
                temp+=fst_kor[k1]
            elif k1 in mid_kor:
                temp+=mid_kor[k1]
            elif k1 in last_kor:
                temp+=last_kor[k1]
            else:
                temp+=k1
            j=1   # 이 경우엔 바로 다음 글자로 넘어가니까 jump 1
        i+=j   # 위에서 받아온 jump를 i에 더해주어 while loop를 진행한다.
    
    # temp에는 'ㅅㅏㄱㅘ' 처럼 자모가 분리되어있다. 
    return join_jamos(temp)   #자모 합치기
```


```python
sd['engkor'] = sd['keyword'].apply(lambda x: engkor(x) if type(x)==str else '')
```

3. 영문으로만 이루어진 키워드 찾기  
영어가 포함된 한글 키워드도 어중간하게 변화되어버렸다.  
해당 키워드들을 구분짓기 위해 영문으로만 구성된 키워드를 표시해둔다.


```python
import re

# 영문으로만 이루어진 키워드 찾기
com = re.compile('^[a-zA-Z0-9]+$')
sd['eng'] = sd['keyword'].apply(lambda x : 'eng' if type(x) == str and com.search(x)!= None else 'not')
```


```python
sd[['keyword', 'engkor', 'eng']].sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keyword</th>
      <th>engkor</th>
      <th>eng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57625</th>
      <td>unix</td>
      <td>ㅕㅜㅑㅌ</td>
      <td>eng</td>
    </tr>
    <tr>
      <th>164850</th>
      <td>사운드바 스피커</td>
      <td>사운드바 스피커</td>
      <td>not</td>
    </tr>
    <tr>
      <th>144058</th>
      <td>wd 외장</td>
      <td>ㅈㅇ 외장</td>
      <td>not</td>
    </tr>
    <tr>
      <th>195377</th>
      <td>베이킹 주걱</td>
      <td>베이킹 주걱</td>
      <td>not</td>
    </tr>
    <tr>
      <th>107552</th>
      <td>후방거울</td>
      <td>후방거울</td>
      <td>not</td>
    </tr>
  </tbody>
</table>
</div>




```python
sd.to_excel('한영변환_210128.xlsx', index = False)
```
