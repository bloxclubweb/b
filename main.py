
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

# ID do canal onde o bot deve criar tópicos
CANAL_ID = 1339793296821850233

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible)
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == CANAL_ID:
        # Cria um tópico na mensagem do usuário
        thread = await message.create_thread(name="Comentários")
        
        # Adiciona reações à mensagem
        await message.add_reaction("<:like:1339794235481657394>")
        await message.add_reaction("<:deslike:1339794237977268264>")

    await client.process_commands(message)

# Inicia o bot
client.run(TOKEN)
