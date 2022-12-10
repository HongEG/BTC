import discord, asyncio, os
from recipe_detail import *
from mybar import *
from discord.ext import commands

token = 'MTAzNzU3MTU3MTczNDI4NjM3Ng.GDkawu.oCrI6rSwntuQ68P8s6FLoBF5OwS_F_NyV_NsiQ'
client = discord.Client()
bot = commands.Bot(command_prefix="$") #접두사를 $로 지정

@bot.event
async def on_ready():
    print("DIscord Bot online!")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
        
#봇 처음 실행시 나타나는 메뉴, 기능1:마시기 기능 -> 조회 / 랜덤 추천 - 칵테일 , 기능 2:My bar 관리 기능 3:도움되는 사이트
@bot.command()
async def welcome(ctx):
    embed = discord.Embed(title = "BTC", description = "어떤 기능을 사용할지 선택", color = 0x62c1cc)
    embed.add_field(name = "마시자!", value = "칵테일 레시피 조회($recipe), 랜덤한 칵테일 추천($random)", inline = False)
    embed.add_field(name = "My bar", value = "나만의 bar를 관리해보자, 재고관리($mybar)", inline = False)
    embed.add_field(name = "더 나은 칵테일 생활을 위헤", value = "각종 도움되는 사이트 및 자료들 url($url)", inline = False)
    await ctx.send(embed = embed)

#!recipe 입력시 나오는 메뉴, 이름, 재료, 카테고리, 잔, 별점 기반으로 검색이 가능하게
@bot.command()
async def recipe(ctx):
    embed = discord.Embed(title = "레시피 메뉴", color = 0x62c1cc)
    embed.add_field(name = "$detail name 칵테일 이름", value = "칵테일 이름에 맞는 칵테일 조회", inline = False)
    embed.add_field(name = "$detail category 카테고리", value = "칵테일 카테고리에 맞는 칵테일 조회", inline = False)
    embed.add_field(name = "$detail glass 잔", value = "칵테일 잔에 맞는 칵테일 조회(영어), 잔 예시는 $glasslist", inline = False)
    embed.add_field(name = "$rating 별점", value = "일정 별점 이상인 칵테일 조회(영어)", inline = False)
    await ctx.send(embed = embed)
    
@bot.command()
async def glasslist(ctx):
    embed = discord.Embed(title = "잔 목록", description = glass_list)
    await ctx.send(embed = embed)

#detail option value 했을때의 각 상황에 맞는 embed 출력 -> 계산 및 출력은 recipe_detail.py 파일에서 하자(미구현)
@bot.command()
async def detail(ctx, option1 , *option2):
#공백 있을 시 제거를 위해 전체를 받은 뒤 join 해준다.
    args = ' '.join(option2)
    args_int = option2
    if(option1 == "name"):  
        embed = discord.Embed(title = "칵테일 이름" , description = args , color = 0x62c1cc)
        embed.add_field(name = "Recipe : ", value = same_name(args)[0], inline = False)
        embed.add_field(name = "Mixing instruction : ", value = same_name(args)[1], inline = False)
        await ctx.send(embed = embed)
    elif(option1 == "ingredient"):
        await ctx.send(embed = embed)
    elif(option1 == "category"):
        same = category(args)
        embed = discord.Embed(title = "칵테일 카테고리" , description = args , color = 0x62c1cc)
        for i in range (0, len(same)):
            embed.add_field(name = "Name", value = same[i], inline = False)
        await ctx.send(embed = embed)
    elif(option1 == "glass"):
        embed = discord.Embed(title = "칵테일 잔: ", description = args, color = 0x62c1cc)
        same = (glass(args)[0 : len(glass(args))])
        for i in range (0, len(same)):
            embed.add_field(name = "Name", value = same[i], inline = False)
        await ctx.send(embed = embed)

@bot.command()
async def rating(ctx, number:float):
    embed = discord.Embed(title = float(number) + "점보다 높은 칵테일 : ", color = 0x62c1cc)
    same_rating = (rating_cocktail(float(number))[0 : len(rating_cocktail(float(number)))])
    for i in range (0, len(same_rating)):
        embed.add_field(name = "Name", value = same_rating[i], inline = False)
    await ctx.send(embed = embed)
            

#random 입력시 cocktail_racipe 1열에서 랜덤 하나를 뽑아서 그 행의 칵테일을 출력해준다.(미구현)
@bot.command()
async def random(ctx):
    embed = discord.Embed(title = "칵테일 이름", description = (cocktail_random()[0]))
    embed.add_field(name = "Recipe : ", value = cocktail_random()[1], inline = False)
    embed.add_field(name = "Mixing instruction : ", value = cocktail_random()[2], inline = False)
    embed.add_field(name = "Category : ", value = cocktail_random()[3], inline = False)
    embed.add_field(name = "Glass : ", value = cocktail_random()[4], inline = False)
    embed.add_field(name = "Rating : ", value = cocktail_random()[5], inline = False)
    
    await ctx.send(embed = embed)

#mybar 입력시 새로운 메뉴 출력 -> 1.현재 재고 확인, 2. 재고 추가 3. 제작 가능 칵테일 4. 추천?, mybar.py에서 하자
@bot.command()
async def mybar(ctx):
    embed = discord.Embed(title = "My bar!", description = "나만의 개인 바 설정!")
    embed.add_field(name = "$stock : ", value = "현재 창고에 있는 칵테일들 목록 보기!", inline = False)
    embed.add_field(name = "$add 칵테일 정보 : ", value = "칵테일 목록에서 추가할 칵테일 입력 (양식 : 이름,양,가격,카테고리,구매일자)", inline = False)
    embed.add_field(name = "$delete 번호: ", value = "삭제할 리스트의 번호 입력!", inline = False)
    embed.add_field(name = "$edit 위치 값: ", value = "수정하려는 위치 입력(열,행)한 뒤 바꿀 값을 입력!", inline = False)
    await ctx.send(embed = embed)

@bot.command()
async def stock(ctx):
    await ctx.send(bar_stock())

@bot.command()
async def add(ctx, option):
    await ctx.send(bar_add(option))

#아 인트는 number로 입력받는구나
@bot.command()
async def delete(ctx, number:int):
    bar_delete(int(number))
    await ctx.send(bar_stock())

#url 입력시 여러 사이트 출력 및 정리된 엑셀 다운로드 링크, 그 외 링크들 출력 
@bot.command()
async def url(ctx):
    embed = discord.Embed(title = "도움이 되는 url", description = "BTC 제작 도움 및 그 외 칵테일 제작에 도움이 되는 사이트들")
    embed.add_field(name = "$stock : ", value = "현재 창고에 있는 칵테일들 목록 보기!", inline = False)
    embed.add_field(name = "$stock : ", value = "현재 창고에 있는 칵테일들 목록 보기!", inline = False)
    embed.add_field(name = "$stock : ", value = "현재 창고에 있는 칵테일들 목록 보기!", inline = False)
    embed.add_field(name = "$stock : ", value = "현재 창고에 있는 칵테일들 목록 보기!", inline = False)

bot.run(token)

