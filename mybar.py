import pandas as pd
#stock -> 현재 리스트 출력 /  리스트에 추가 / 제거 / 수정 기능 -> 입력값은 , 으로 구분  / manu -> 제작가능
#구현예정 -> 이름 입력시 그와 관련된 정보 출력(ex: milk liquere는 보관기한이 6개월~1년, 실온 보관 추천 등등...)

def bar_stock():       
    my_bar = pd.read_csv('my_bar.csv')       
    return my_bar 

def bar_add(value):
    my_bar = pd.read_csv('my_bar.csv')
    df = pd.DataFrame(data=my_bar)
    add_value = value.split(',')
    df.loc[df.shape[0]] = [add_value[0], add_value[1], add_value[2], add_value[3], add_value[4]]
    df.to_csv('my_bar.csv', index=False)
    return bar_stock()
    

#삭제하려는 행 입력
def bar_delete(value):
    my_bar = pd.read_csv('my_bar.csv')
    df = pd.DataFrame(data=my_bar)
    delete_my_bar = my_bar.drop(index=value)
    df2 = pd.DataFrame(data=delete_my_bar)
    df2.to_csv('my_bar.csv', index=False)

#수정하려는 행과 열 입력 후 값 수정(미구현)
def edit():
    return