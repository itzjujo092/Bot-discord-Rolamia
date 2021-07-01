import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from datetime import datetime
import os
import aiohttp
import re
from datetime import timedelta
import traceback
import sys
from random import choice, randint
import json
from datetime import datetime
from discord import Embed
import random
import asyncio


intents = discord.Intents.default()
intents.guild_reactions = True
intents.guild_messages = True
intents.messages = True





TOKEN = "Nzc3OTQzNzcxNjU1ODMxNTYy.X7KymA.n_U3Op-PckGVrTF9m_rqetisJNo"
bot = commands.Bot(command_prefix = "°",help_command=None)
client= commands.Bot(command_prefix = "°", help_command=None)

@bot.command()
async def setprefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"**Se cambio el prefix a ``{prefix}``**")    
    

@bot.event
async def on_ready():
    print("Hola mundo")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="°help | "f"{len(bot.guilds)} servers!"))

@bot.event
async def on_message_delete(message):
	bot.sniped_messages[messages.guild.id] = (message.content, messages.author, message.channel.name, messages.created_at)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embed=discord.Embed(title="", description="**No se encuentra este comando en mi lista!, Verifica tu comando**")
		await ctx.send(embed=embed)
#------------------------------------------ Parte De ayuda -----------------------------------------
@bot.command()
async def informacion(ctx):
    embed = discord.Embed(title="Informacion del bot", description= "La informacion del bot esta aqui:")
    embed.add_field(name="Informacion", value="El bot fue creado el 16 de noviembre de 2020 por un usuario que le encanta hacer bots y con la esperanza de hacer este bot para mejorar todos los servidores con distintas funciones")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def creador(ctx):
	embed = discord.Embed(title="Creador", description= "Aqui vas a ver la informacion de mi creador! ")
	embed.add_field(name="Creador",value="El creador es itzjujo092 de 13 años, inteligente y que le gusta mucho programar,tiene su canal de YT y TW y que tiene como tag de discord itzjujo092YT#6043")
	embed.add_field(name="Canal de Youtube",value="El canal de YT es:     https://www.youtube.com/channel/UCzk3btKapWwjd7jeEpMSDkA?view_as=subscriber")
	embed.add_field(name="Canal de Twitch",value="El canal de Twitch es:    https://twitch.tv/itzjujo095")
	embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/iEjeY19LBRE_Mt6qEOHQVvPCGPQ5NeTgyPhTh7rQsuA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/500496397540392961/5c8a2141f6afab96eb1207ba58318808.webp")
	await ctx.send(content=None, embed=embed)		



@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Ayuda", description= "Aqui se pueden ver todas las opciones de ayuda sobre el bot")
    embed.add_field(name="comandos", value="Mira los comandos que puedes utilizar del bot")
    embed.add_field(name="informacion", value="Mira la informacion sobre este bot")
    embed.add_field(name="creador", value="Mira el creador de este fantastico bot y todas sus redes sociales!")
    embed.add_field(name="botsoporte", value="Aqui esta el apartado donde puedes ver la parte de soporte que contiene el bot")
    embed.add_field(name="prefix", value="Entra aqui para cambiar el prefix del bot en tu server")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title="Comandos", description= "Aqui se encuentran los comandos que posee nuestro bot")
    embed.add_field(name="moderacion", value="Dale click para que veas todos los comandos de moderacion")
    embed.add_field(name="entretenimiento", value="Aqui se ven los comandos de entretenimiento")
    embed.add_field(name="calculadora", value="Oh, Sorpresa, El propio bot tiene calculadora! usala")
    await ctx.send(content=None, embed=embed)

	
@bot.command()
async def prefix(ctx):
	embed = discord.Embed(title="Cambia el prefix", description= "El comando para cambiar el prefix es el siguiente:")
	embed.add_field(name="setprefix", value="Ahi pones despues del prefix el simbolo y/o numero que quieras")
	await ctx.send(content=None, embed=embed)
#--------------------------------- Botsoporte ---------------------------------------------------
@bot.command()
async def botsoporte(ctx):
	embed = discord.Embed(title="Bot", description="Aqui puedes ver todo lo que tiene que ver con la parte de soporte del bot")
	embed.add_field(name="invite", value="Si quieres tener el bot rolamia en tu server mira este comando!")
	embed.add_field(name="serversoporte", value="Aqui en este comando tu puedes ver el server de soporte !")
	embed.add_field(name="paginasoporte", value="Aqui esta la pagina web de soporte")	
	embed.add_field(name="topggpagina", value="Aqui esta la pagina oficial del Bot en Top gg")
	embed.add_field(name="servers", value="Aqui puedes mirar en cuantos servers esta el bot! ")
	embed.add_field(name="ping", value="Mira el ping del bot en este apartado")
	embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/tiIi9CfcMG9FkrwuQ1HQ7iZWTG3vauhWDqzr-VDiIzM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/777943771655831562/5c44863ceb2ad0c24f6c653274da7c67.webp?width=475&height=475")
	await ctx.send(content=None, embed=embed)

@bot.command()	
async def servers(ctx):
	embed = discord.Embed(title="Servers", description="Aqui puedes mirar los servers en que esta el bot! ")
	embed.add_field(name="La cantidad de servers es: ", value=f"{len(bot.guilds)} servers!")
	await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def ping(ctx):
	embed = discord.Embed(title="Ping del Bot", description="Mira el ping del bot! ")
	embed.add_field(name="Ping!", value=f"{round(bot.latency*1000)} de ping Tengo! ")
	embed.set_thumbnail(url="https://andinalink.com/wp-content/uploads/2018/07/internet_de_las_cosas-785x500.jpg")
	await ctx.send(embed=embed)	

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invitacion", description= "La invitacion del bot para que este en tu servidor aqui esta!")
    embed.add_field(name="invitacion", value="El ID de invitacion es: https://discord.com/oauth2/authorize?client_id=777943771655831562&scope=bot&permissions=36723712")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def serversoporte(ctx):
	embed = discord.Embed(title="Server para el soporte", description="Aqui esta el server de soporte ")
	embed.add_field(name="server", value="https://discord.gg/9MWTmcVJep")
	await ctx.send(embed=embed)

@bot.command()
async def paginasoporte(ctx):
	embed = discord.Embed(title="Pagina de soporte del bot", description="La pagina de soporte")
	embed.add_field(name="pagina web", value="https://rolamiabotofficial7.webnode.es")
	await ctx.send(embed=embed)

@bot.command()
async def topggpagina(ctx):
	embed = discord.Embed(title="Pagina de top gg", description="topgg La pagina donde esta legalmente verificado el bot")
	embed.add_field(name="Pagina topgg", value="https://top.gg/bot/777943771655831562")
	await ctx.send(embed=embed)	
#--------------------------------- Comandos de Moderacion ---------------------------------------
@bot.command()
async def moderacion(ctx):
  embed = discord.Embed(title="moderacion", description="Aqui estan todos los comandos de moderacion que puedes usar")
  embed.add_field(name="kick", value="Dale una expulsion a un usuario, pero se puede volver a unir a el servidor")
  embed.add_field(name="ban", value="Banea o expulsa permanentemente a una persona de tu servidor ")
  embed.add_field(name="clear", value="Elimina la cantidad de mensajes que elijas !")
  embed.add_field(name="slowmode", value="Cambia el modo pausado de un canal!, Se cuenta en segundos")
  await ctx.send(embed=embed)			

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
	if not member:
		await ctx.send ("*Por favor especifique el miembro*")
		return
	await member.kick()
	await ctx.send(f"**{member.mention} ha sido kickeado**")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
	if not member:
		await ctx.send ("*Por favor especifique el miembro*")
		return
	await member.ban()
	await ctx.send(f"**{member.mention} ha sido Baneado**")
	
@bot.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
	await ctx.send (f"**{amount} mensajes eliminados**")
	await ctx.channel.purge(limit=1)

@bot.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"**Se a cambiado el modo pausado a: {seconds} segundos! **")
#---------------------------------- Comandos De Entretenimiento -----------------------------------------

@bot.command()
async def entretenimiento(ctx):
	embed = discord.Embed(title="Comandos de entretenimiento", description= "Aqui puedes ver todos los comandos de entretenimiento que tiene el bot!")
	embed.add_field(name="poll", value="Has encuestas con el comando poll super facil! Pones poll y pones el nombre de la encuesta")
	embed.add_field(name="avatar", value="Mira el avatar de el usuario o ID que menciones! Se ve y muy facil")
	embed.add_field(name="decir", value="Manda a decir con el bot las cosas que quieras!!!")
	embed.add_field(name="userinfo", value= "Mira la informacion del usuario")
	embed.add_field(name="snipe", value="Mira algun mensaje eliminado con este comando")
	await ctx.send(embed=embed)	

@bot.command()
async def decir(ctx, *, arg):
	await ctx.send(arg)	
	await ctx.message.delete()

@bot.command()
async def userinfo(ctx, *, member: discord.Member):
	def format_time(time):
	    return time.strftime("%d-%B-%Y %I:%M %p")

	member = member if member else ctx.author

	# datetime.datetime + datetime.timedelta(hours=5, minutes=30)

	# member.status

	# member.activity

	embed = discord.Embed( 
	    title=f"{member.name} Info:", color=discord.Color.blurple())

	embed.set_thumbnail(url=member.avatar_url)

	embed.add_field(name="ID del usuario", value=member.id, inline=False)	

	embed.add_field(name="Registrado", value=format_time(
		member.created_at), inline=False)

	embed.add_field(name="Unido ", value=format_time(
		member.joined_at), inline=False)	
    
	sorted_roles = sorted(
		[role for role in member.roles[1:]], key=lambda x: x.position, reverse=True)

	embed.add_field(name="Roles", value=", ".join(
		role.mention for role in sorted_roles), inline=False)

	await ctx.send(embed=embed)

@bot.command()
async def poll(ctx,*,message):
	emb=discord.Embed(title="Encuesta", description=f"{message}")
	msg=await ctx.channel.send(embed=emb)
	await msg.add_reaction("👍")
	await msg.add_reaction("👎")


@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

bot.sniped_messages = {}

@bot.command()
async def snipe(ctx):
	contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]

	embed = discord.Embed(description=f"{snipe_message_content}")
		embed.set_footer(text=f"Pedido hecho de: {message.author.name}#{message.author.discriminator}")
		embed.set_author(name = f"El mensaje snipeado es de: {snipe_message_author}")
		await message.channel.send(embed=embed)
		return
		

#------------------------------------ Comandos De La Calculadora-----------------------------

@bot.command()
async def calculadora(ctx):
    embed = discord.Embed(title="Comandos de la calculadora", description= "Aqui se pueden ver todos los comandos de la calculadora que el bot tiene integrado")
    embed.add_field(name="suma", value="Suma 2 variables sin necesidad del signo de + totalmente legitimo ")
    embed.add_field(name="resta", value="Resta 2 variables sin necesidad del signo de - totalmente legitimo ")
    embed.add_field(name="multiplicacion", value="Multiplica 2 variables sin necesidad del signo de * totalmente legitimo ")
    embed.add_field(name="division", value="Divide 2 variables sin necesidad del signo de / totalmente legitimo  ")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def suma(ctx,arg1,arg2):
	suma = int(arg1) + int(arg2)
	await ctx.send(suma)

@bot.command()
async def multiplicacion(ctx,arg1,arg2):
	multiplicacion = int(arg1) * int(arg2)
	await ctx.send(multiplicacion)

@bot.command()
async def resta(ctx,arg1,arg2):
	resta = int(arg1) - int(arg2)
	await ctx.send(resta)

@bot.command()
async def division(ctx,arg1,arg2):
	division = int(arg1) / int(arg2)
	await ctx.send(division)


bot.run(TOKEN)
client.run(TOKEN)