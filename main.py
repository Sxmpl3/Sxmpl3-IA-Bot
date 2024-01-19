import os
from colorama import Fore

try:
    import discord
    import openai
    from discord import Embed
    from discord.ext import commands
except ModuleNotFoundError:
    os.system("pip install discord")
    os.system("pip install openai")

    import discord
    import openai
    from discord import Embed
    from discord.ext import commands

openai.api_key = 'api key'

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.wait_until_ready()

    channel_id = 1197840689434722344
    channel = bot.get_channel(channel_id)

    print(f"{Fore.RED}[+]{Fore.RESET} Sxmpl3 IA bot")
    print(f"{Fore.RED}[+]{Fore.RESET} Conectado como: {bot.user.name}")

    if channel:
        embed = Embed(title="Sxmpl3`s IA Bot | Created by Sxmpl3", color=0x00ff00)
        embed.add_field(name="Online", value="Bot Online", inline=False)
        embed.add_field(name="Comandos", value="- $ayuda\n- $q <pregunta>", inline=False)

        await channel.send(embed=embed)
    else:
        print(f"{Fore.RED}[!]{Fore.RESET} No se pudo encontrar el canal con ID: {channel_id}")

@bot.command()
async def ayuda(ctx):
    channel_id = 1197840689434722344
    channel = bot.get_channel(channel_id)

    author = ctx.author.mention
    embed = Embed(title="Sxmpl3`s IA Bot | Created by Sxmpl3", color=0x00ff00)
    embed.add_field(name="\u200B", value=f"- ¡Hola {author}!\n- Utilice el comando $q <pregunta> para obtener respuestas.", inline=False)

    await channel.send(embed=embed)

@bot.command()
async def q(ctx, *args):
    channel_id = 1197840689434722344
    channel = bot.get_channel(channel_id)

    pregunta = ' '.join(args)
    author = ctx.author.name

    messages = [
        {"role": "system", "content": "You are a IA bot."},
        {"role": "user", "content": f"{author}: {pregunta}"}
    ]

    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    respuesta_texto = respuesta['choices'][0]['message']['content'][:1024]

    author_mention = ctx.author.mention
    embed = Embed(title="Sxmpl3`s IA Bot | Created by Sxmpl3", color=0x00ff00)
    embed.add_field(name="\u200B", value=f"{respuesta_texto}", inline=False)
    embed.add_field(name="\u200B", value=f"- {author_mention} - Espero haber respondido su pregunta de forma exitosa.", inline=False)

    await channel.send(embed=embed)
    
bot.run('token')
