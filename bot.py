import discord
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
    
def help_coin():
    return "Команды: $hello, Hi!, $pass, $bye, $coin, $smile"

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
        await message.channel.send("Hi!")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$help'):
        await message.channel.send(help_coin())
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$coin"):   
        await message.channel.send(flip_coin())
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTE1MjU3Mzk3NDU1MTc0NDY1NQ.Ga6N5S.ApoYV-WjSCPBj9CRH54gJtubTK0eX8mUy-Nnrs")
 
