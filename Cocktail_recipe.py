import requests, re, csv
from bs4 import BeautifulSoup as bs

cocktail_list = []
cocktail_recipe = []
cocktail_mixing = []
cocktail_glass = []
cocktail_rating = []
cocktail_category = []
html_tag_small = []

#header에 User_info를 추가해 봇이 아님을 증명하고, 데이터를 뽑을 수 있게 만들어준다.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url_base ='https://www.webtender.com/db/drink/'
f = open('cocktail.csv','w', newline='')
wr = csv.writer(f)

#for문을 이용한 칵테일 레시피 1~6217까지 url + i로 검색해준다.
for i in range(1, 1000):
    url = url_base + str(i)
    soup = requests.get(url, headers = headers).text

    html = bs(soup, 'html.parser')
    #str(html.select)로 특정 태그의 데이터 추출 및 re.sub에서 정규표현식 -> 모든 html 태그 제거 
    #특히 recipe의 \n과 mixing에서 ,는 csv 파일을 만들때 오류가 생기기에 수정해준다.
    #category, glass, rating은 small이라는 공통적인 태그 내부에 존재하기에 전체를 불러온뒤, split을 통해 리스트를 분해 각 요소를 저장해준다.
    html_tag_small = ((re.sub('<(/)?([a-zA-Z0-9]*)(\\s[a-zA-Z0-9]*=[^>]*)?(\\s)*(/)?>',' ',str(html.select('td > small')),0).strip("[&]& "))).split(',')
    cocktail_list.append((re.sub('<(/)?([a-zA-Z0-9]*)(\\s[a-zA-Z0-9]*=[^>]*)?(\\s)*(/)?>',' ',str(html.select('h1')),0).strip("[&]& ")))
    cocktail_recipe.append((re.sub('\n|<(/)?([a-zA-Z0-9]*)(\\s[a-zA-Z0-9]*=[^>]*)?(\\s)*(/)?>',' ',str(html.select('ul > li')),0).strip("[&]& &\n&")))
    cocktail_mixing.append((re.sub(',|<(/)?([a-zA-Z0-9]*)(\\s[a-zA-Z0-9]*=[^>]*)?(\\s)*(/)?>',' ',str(html.select('td > p')),0).strip("[&]& ")))
    cocktail_category.append((html_tag_small[0].strip()))
    cocktail_glass.append(html_tag_small[2].strip())
    #점수만을 뽑아내기 위해 strip한 리스트에서 :3을 통해 점수까지만 값을 추출한다.
    cocktail_rating.append((html_tag_small[3].strip())[:3])

#cocktail_recipe.csv파일 생성, 인코딩 방식 지정, 공백 줄 생김 방지를 위한 newline 선언
f = open('cocktail_recipe.csv','w',encoding='UTF-8', newline='')
f.write("Name,Recipe,Mixing insturction,Category,Glass,Rating\n")
for i in range(len(cocktail_list)):
    # 각 요소 사이에 직접 ,를 넣어주고 마지막에 \n을 넣어서 행을 구분해준다.
    f.write(cocktail_list[i] + ',' + cocktail_recipe[i] + ',' + cocktail_mixing[i] + ',' + cocktail_category[i] + ',' + cocktail_glass[i] + ',' + cocktail_rating[i] + '\n')
    
f.close()