import random
import discord
import os
from discord.ext import commands
from bot_token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
bilgiler = [
    "Eski eşyaları çöpe atmak yerine geri dönüştürün.",
    "Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.",
    "Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.",
    "Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.",
    "Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın.",
    "Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.",
    "Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve ayaklarınızı (mümkün olduğunda) kullanmaya çalışın."
]

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum! Benim görevim geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi vermek. $bilgi yazarak geri dönüşüm hakkında bilgiler alabilirsiniz. ')

@bot.command()
async def bilgi(ctx):
    await ctx.send (random.choice(bilgiler))

@bot.command()
async def random_gorsel(ctx):
    image_list = os.listdir('M2L2/geri_donusum_gorsel')
    image_name = random.choice(image_list)

    with open(f'M2L2/geri_donusum_gorsel/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("İşte senin için bir görsel:", file =picture)      




bot.run(token)
