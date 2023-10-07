import discord
import random
import os
import requests




def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
    
def help_coin():
    return "Команды: $hello, Hi!, $pass, $bye, $coin, $smile, mem, animal, duck"

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("$Hi!")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$help'):
        await message.channel.send(help_coin())
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("coin"):   
        await message.channel.send(flip_coin())
    elif message.content == "mem":
        name = random.choice(os.listdir('images'))
        with open(f'images/{name}', 'rb') as f:
            picture = discord.File(f)   
        await message.channel.send(file=picture)
    elif message.content == "animal":
        nam = random.choice(os.listdir('animals'))
        with open(f'animals/{nam}', 'rb') as f:
            picture = discord.File(f)   
        await message.channel.send(file=picture)
    elif message.content.startswith("duck"):
        image_url = get_duck_image_url()
    await message.channel.send(image_url) 
    
    
    
client.run("MTE1MjU3Mzk3NDU1MTc0NDY1NQ.GAcboz.6Z1CQ4zKDvFLtkbt__fzofzVgvzrEm10RofMhg")
