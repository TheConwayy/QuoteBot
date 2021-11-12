import discord
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import json

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

def getrandquote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = '>>> "' + json_data[0]['q'] + '" - _' + json_data[0]['a'] + '_'
    return quote

def gettodayquote():
    response = requests.get('https://zenquotes.io/api/today')
    json_data = json.loads(response.text)
    quote = '>>> "' + json_data[0]['q'] + '" - _' + json_data[0]['a'] + '_'
    return quote

client = discord.Client()

@client.event
async def on_ready():
    print('Bot online')

    activity = discord.Activity(type=discord.ActivityType.listening,name="quotes :)")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('"random'):
        quote = getrandquote()
        await message.delete()
        await message.channel.send(f'<@{message.author.id}>\n' + quote, delete_after=15)

    if message.content.startswith('"daily'):
        quote = gettodayquote()
        await message.delete()
        await message.channel.send(f'<@{message.author.id}>\n' + quote, delete_after=15)


    if message.content.startswith('"api'):
        await message.delete()
        embed = discord.Embed(title='API', color=0xECF0F1, description='Interested in the API that Quote Bot uses?\n\nYou can find it [here](https://zenquotes.io/)')

        await message.channel.send(f'<@{message.author.id}>', embed=embed, delete_after=10)

    if message.content.startswith('"invites'):
        await message.delete();

        embed = discord.Embed(title='Invites', color=0xECF0F1, description='[Support Discord](https://conwaysolutions.net/quotebot/discord)\n[Bot Invite](https://conwaysolutions.net/quotebot/)')

        await message.channel.send(f'<@{message.author.id}>', embed=embed, delete_after=10)


    if message.content.startswith('"links'):
        await message.delete()
        
        embed = discord.Embed(title='Links', color=0xECF0F1, description='[Support Discord](https://conwaysolutions.net/quotebot/discord)\n[Bot Invite](https://conwaysolutions.net/quotebot)\n[Github](https://conwaysolutions.net/quotebot/github)\nConway Solutions (developing company) [Discord](https://conwaysolutions.net/discord/)\n_Conway Solutions is the company that released and developed this bot_')

        await message.channel.send(f'<@{message.author.id}>', embed=embed, delete_after=15)
        

    if message.content.startswith('"help'):
        await message.delete()

        embed = discord.Embed(title='Quote Bot\'s Commands', color=0xECF0F1, description='All commands able to be used for the Quote Bot')
        embed.add_field(name='"daily', value='Displays the QoTD (Quote of The Day) | This command will return a new quote everyday', inline=True)
        embed.add_field(name='"random', value='Displays a random quote | This command will display a quote at random', inline=True)
        embed.add_field(name='"invites', value='Displays all invites related to Quote Bot | This command will return invites', inline=False) 
        embed.add_field(name='"links', value='Displays all links related to Quote Bot | This command will return links', inline=True)
        embed.add_field(name='"api', value='Displays information about the API used | This command will return to you a link to website for the API used', inline=False)
        embed.add_field(name='"help', value='The help command | This commands displays all available commands', inline=False)
        
        aembed = discord.Embed(title='About', color=0xECF0F1, description='Sometimes all you _(or even other people in your server)_ need is a nice quote to help get you through the day. And, that\'s where I come in!', inline=False)
        aembed.add_field(name="Invite", value='You can invite the bot [here](https://top.gg/bot/903688503257337928) _(this is a [top.gg](https://top.gg/) link)_')
        aembed.add_field(name='Plans for this bot', value='If this bot gets any up-votes and some feedback from the community saying that they want more, well, I\'ll give you more!!\nI also plan on adding some more here and there.. But, I would love to hear from you all!', inline=False)

        await message.author.send('**Here are the commands available:**', embed=embed)
        await message.author.send(embed=aembed)
        await message.channel.send(f'>>> <@{message.author.id}>, you\'ve got mail! :mailbox_with_mail:', delete_after=5)


TOKEN = os.getenv('TOKEN')
client.run(TOKEN)

