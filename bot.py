import discord
from M1L4.bot_token import TOKEN
from gen_pass import gen_pass
#from dosya_adi import değişken/fonksiyon_adi

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642") # unicode
    elif message.content.startswith('$yonca'):
        await message.channel.send("Selamlar eğitmenim!")
    elif message.content.startswith('$parola'):
        await message.channel.send(f"Parolan: {gen_pass(10)}")
    #else:
    #    await message.channel.send(message.content)

client.run(TOKEN)