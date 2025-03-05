import discord
import random
from discord.ext import commands

# Configura el bot con el prefijo $
intents = discord.Intents.default()
intents.messages = True  # Habilitar permisos de mensajes
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

@bot.command()
async def que(ctx, *, frase: str):
    # Verifica que la frase tenga al menos 5 palabras
    if len(frase.split()) < 5:
        await ctx.send(f'{ctx.author.mention} Tu frase debe tener al menos 5 palabras.')
        return
    
    # Elige aleatoriamente entre Sí y No
    respuesta = random.choice(['Sí', 'No'])
    await ctx.send(f'{ctx.author.mention} {respuesta}')

# Reemplaza 'TU_TOKEN_AQUI' con tu token real
bot.run('TU_TOKEN_AQUI')