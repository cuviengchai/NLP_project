import discord
import yaml

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # ignore own message
    print(message)
    
    if message.author == client.user:
        return
    if message.content == 'ping':
        await client.send_message(message.channel, 'pong')
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)



with open('config.yml', 'r') as f:
    config = yaml.load(f)

client.run(config['token'])
