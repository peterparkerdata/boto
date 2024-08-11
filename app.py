from dotenv import load_dotenv
import discord
import os

# Load environment variables from .env file
load_dotenv()

token = os.getenv('TOKEN')
if not token:
    print("Error: TOKEN environment variable is not set.")
else:
    print(f'TOKEN loaded successfully: {token}')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure that your bot can read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hi'):
        await message.channel.send('Hola!')

client.run(token)
