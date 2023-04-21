import discord
import requests
from io import BytesIO

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logado como {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!send_image'):
        image_url = 'image-url' # substitua pelo URL da imagem desejada
        response = requests.get(image_url)
        image_data = BytesIO(response.content)
        file = discord.File(fp=image_data, filename='name.png')
        sent_message = await message.channel.send(file=file)
        await sent_message.add_reaction('\U0001F310')

    if message.content.startswith('!send_image2'):
        image_url = 'image-url' # substitua pelo URL da imagem desejada
        response = requests.get(image_url)
        image_data = BytesIO(response.content)
        file = discord.File(fp=image_data, filename='name.png')
        sent_message = await message.channel.send(file=file)
        await sent_message.add_reaction('✅')

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1234: # substitua MESSAGE_ID pelo ID da mensagem que você deseja monitorar
        guild = client.get_guild(payload.guild_id)
        role = guild.get_role(1234) # substitua ROLE_ID pelo ID do cargo que você deseja adicionar
        member = guild.get_member(payload.user_id)
        await member.add_roles(role)

    if payload.emoji.name == '✅':
        guild = client.get_guild(payload.guild_id)
        role = guild.get_role(1234) # vai reprovar no exame final otaria que você deseja adicionar
        member = guild.get_member(payload.user_id)
        await member.add_roles(role)

# Inicie o bot
client.run('your token code')
