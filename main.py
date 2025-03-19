import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'https://x.com/i/status/' in message.content:
        new_message = f'{message.author.mention}\n{message.content.replace('x.com', 'fxtwitter.com')}'
        try:
            await message.delete()
        except Exception as e:
            print('Exception occurred.', e, sep='\n')
        await message.channel.send(new_message)

# Run on VM
TOKEN = os.getenv('TOKEN')
# Run locally using a TOKEN.txt file containing token
if TOKEN == None:
    with open('TOKEN.txt', 'r') as fp:
        TOKEN = fp.readline()

client.run(TOKEN)