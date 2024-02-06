import discord
from discord.ext import commands
import random
from googleapiclient.discovery import build

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "$", intents=intents)   #指令前標示
api_key = "SEARCH API KEY"     #custom search api key

@client.event
async def on_ready():
    print("!!! Bot is Online!!!\n")

@client.command(aliases = ["show"])         #指令 => $ + show = $show
async def showpic(ctx, *, search):
    #ran = random.randint(0,1)       #似乎不是指定圖片順序 排序部分似乎是點擊率高低的樣子
    resource = build("customsearch", "v1", developerKey = api_key).cse()
    result = resource.list(q=f"{search}", cx = "b946ce0d8a88e774b", searchType = "image").execute()          #search engine ID


    ran = 1
    for i in range(1,9,1):
        if "lookaside" in result["items"][i]["link"] or "dcard" in result["items"][i]["link"] or "licdn" in result["items"][i]["link"]:
            i = i+1
        else:
            ran = i
            break


    url = result["items"][ran]["link"]
    print(url)

    embed1 = discord.Embed(title = f"Here's your image ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed = embed1)


client.run("Discord bot token")  #discord bot token