import pandas as pd
import random

glass_list = ['Beer mug', 'Beer pilser', 'Brandy snifer', 'Champagne flute', 'Cocktail glass', 'Coffee mug', 'Colins glass', 'Cordial glass', 'Highball glass', 'Hurricane glass', 'Irish coffee cup','Margrita/Coupette glass', 'Mason jar', 'Old-fashioned glass', 'Parfait glass', 'Pint glass', 'Pitcher', 'Piusse cafe glass', 'Punch bowl', 'Red wine glass', 'Sherry glass', 'Shot glass', 'Whiskey sour glass','Whith wine glass', 'Unknown glass type']
cocktail_list = pd.read_csv('Cocktail_recipe.csv')

#name은 값을 입력받아서 첫 줄과 확인해서 단어 단위로 같은 이름이 있으면 출력 ex) milk -> kahlua milk, ~~ milk milk ~~
#비슷한 결과를 아래 띄워주는 기능을 구현해보자? -> 이거를 OSS로 찾아보는것도?
def same_name(value):
    number = 0
    same_name = []
    for i in range(len(cocktail_list['Name'])):
        if value == cocktail_list['Name'][number]:
            same_name.append(cocktail_list['Recipe'][number])
            same_name.append(cocktail_list['Mixing insturction'][number])
        number = number + 1
    return same_name
        
#ingredient는 Recipe에서 값 비교 후 이름이 같은 것이 있을떄만 출력 
def ingrdient(value):
    return value

#category는 값 비교 후 같은 것들 출력, 필요한가?, 이름만 출력
def category(value):
    number = 0
    same_cate = []
    for i in range(len(cocktail_list['Category'])):
        if value == cocktail_list['Category'][number]:
            same_cate.append(cocktail_list['Name'][number])
        number = number + 1
    return same_cate
#glass도 동일, 대신 이름만 출력(많으니까, 표로 만들거나?)
def glass(value):
    number = 0
    same_glass = []
    for i in range(len(cocktail_list['Glass'])):
        if value == cocktail_list['Glass'][number]:
            same_glass.append(cocktail_list['Name'][number])
        number = number + 1
    return same_glass
        
#좀 더 구현해보자
#rating은 일정 값 이상인 것만 출력 and 오름차순 정렬, 이름이랑 점수랑 같이 표현되게 하려면? -> 2차원 배열으로 작성?, 동적할당 대신 리스트를 2개 쓰자
#음, 근데 리스트를 2개 쓰면 2개 연동을 시켜줘야 정렬을 해도 같이 되는데... 오름차순만 쓸거면 리스트를 미리 정리해
def rating_cocktail(value):
    number = 0
    same_rating = []
    for i in range(len(cocktail_list['Rating'])):
        if value < cocktail_list['Rating'][number]:
            same_rating.append(cocktail_list['Name'][number])
        number = number + 1
    return same_rating
    
#cocktail_random 함수는 1열에서 랜덤으로 하나를 골라서 그 행의 데이터를 출력해준다......
#근데 그냥 #random.choice(cocktail_list['Name'])를 하면 난수갑이 나오니까..숫자 랜덤 -> 맞는 인덱스 행 
def cocktail_random():
    number = random.randrange(0, len(cocktail_list['Name']))
    return cocktail_list.loc[number]

#option = "A. J."
#print(name(option)[1])
#print(category("Ordinary Drink"))
#print(rating(7))
#print(glass("Highball glass"))
#a = (cocktail_random())