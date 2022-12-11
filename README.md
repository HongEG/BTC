# Discord Bot - BTC

### Project Description
- BTC(Bot To Cocktail) -> 😠NOT BITCOIN
- 디스코드에는 다양한 봇들이 있고, 이들은 좋은 접근성과 사용자와 상호작용하기에 좋다는 생각을 하였다. 최근 들인 취미로 홈텐딩을 시작하였는데, 이와 관련된 프로그램또는, 웹페이지, 앱을 한번쯤 생각해봤고, 학교에서 진행한 OSS 수업에서 좋은 기회가 생겨서 프로젝트를 시작하게 되었다.

- Project 초안 
    - discord bot(menu를 통해서 선택 가능하게)
    - 칵테일 랜덤 추천
    - 재료 선택 후 제작 가능 칵테일 목록 뽑아내주기(구현 예정)
    - 재료 랜덤 추천
    - 칵테일에 곁들여 먹는 무언가(구현 예정)
    - 도움되는 사이트 제공(ex : 가니쉬 방법 등등)
    - 나만의 바 기능(id / login 기능)(id / login 기능 구현 예정)
        - 칵테일 재료 추가, 조회, 재고 관리(추가된 날짜, 유통기한, 보관 위치 등)
        - 제작 가능 칵테일 레시피 제공(구현 예정)
        - 칵테일 목록에서 선택 시 제작 방법 상세히 제공 / 사진 웹 검색 제공(구현 예정)

### Files
- BTC.py : 봇 실행 파일, 이벤트, 명령어 코드 구현
- Cocktail_recipe.py : 웹 파싱 및 데이터 가공, csv파일로 작성하는 코드 구현
- recipe_detail.py : csv파일을 읽어서 pandas를 사용한 Dataframe 가공한 데이터 또는 csv파일을 사용해서 사용자의 명령어를 받아서 처리하는 코드 구현
- mybar.py : 사용자의 바를 가상으로 구현, 저장한 데이터 출력, 추가, 삭제 ,수정기능(수정기능 -> 구현 예정)
- cocktail_recipe.csv : 웹 파싱한 데이터
- mybar.csv : 시용자의 가상 바와 관련된 데이터를 저장.

### Usage
- 코드 실행 가이드라인


### Reference
- https://discord.com/developers/docs/intro : 디스코드 공식 api
- https://doohyun.tistory.com/4 : html 모든 태그 제거 
- https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html : pandas 공식 사이트 -> 가이드 참고

- https://ducj.tistory.com/186 : anaconda3 prompt가 사라질 경우 직접 실행하는 방법
- https://luran.me/475 : discord module 오류 생길경우 선행해서 실행할 코드를 참고
- https://pcmc.tistory.com/entry/190311-Bot-Detection-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EC%B0%A8%EB%8B%A8-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EC%9A%B0%ED%9A%8C-1?category=809836 : BeautifulSoup 사용 웹 크롤링시 오류 발생할경우 우회방법에 대한 코드 참고

### License


### Needs to Improvements
- 데이터를 출력하는 방법으로 embed만 과다하게 사용했다. -> button 등 다른 discord 함수로 교체
- ingredient로 검색하는 기능 구현
- 칵테일 제작 과정을 봇과 상호작용 가능하게 구현 -> 이미지(발할라)
