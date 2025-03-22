import os
from flask import Flask
from fnmatch import fnmatch
import discord

app = Flask(__name__)
@app.route('/')
def home():
    return 'Bot is up!'
app.run(host='0.0.0.0', port=8080)

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

    if fnmatch(message.content, '*https://x.com/*/status/*'):
        new_message = f"{message.content.replace('x.com', 'fxtwitter.com')}"

        try:
            await message.delete()
        except Exception as e:
            print('Exception occurred.', e, sep='\n')

        webhook = await message.channel.create_webhook(name=message.author.name)
        await webhook.send(
            new_message, username=message.author.nick, avatar_url=message.author.avatar.url)
        
        webhooks = await message.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()

# Run on VM
TOKEN = os.getenv('TOKEN')
# Run locally using a TOKEN.txt file containing token
if TOKEN == None:
    with open('TOKEN.txt', 'r') as fp:
        TOKEN = fp.readline()

client.run(TOKEN)