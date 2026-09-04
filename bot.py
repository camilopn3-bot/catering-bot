import discord
from discord.ext import commands
import random
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

roles_catering = [
    "a,b,c,e,f"
]
roles_disponibles = roles_catering.copy()
ultimo_dia = datetime.now().date()

@bot.event
async def on_ready():
    print(f'¡El bot {bot.user} está listo y con control de fechas activo!')

@bot.command()
async def tarea(ctx):
    global roles_disponibles, ultimo_dia
    
    dia_actual = datetime.now().date()
    
    if dia_actual != ultimo_dia:
        roles_disponibles = roles_catering.copy()
        ultimo_dia = dia_actual

    if not roles_disponibles:
        await ctx.send("🚫 ¡Las tareas de hoy ya se han agotado por completo! Vuelve a intentarlo mañana.")
        return

    rol_elegido = random.choice(roles_disponibles)
    roles_disponibles.remove(rol_elegido)
    await ctx.send(f'{ctx.author.mention}, tu ROL asignado hoy es: **{rol_elegido}**')

import os
bot.run(os.getenv('DISCORD_TOKEN'))
