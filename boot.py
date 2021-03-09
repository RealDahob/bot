import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix=".")
@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi


client.run('ODE0MDU5NzA4ODY4NDYwNTY1.YDYWLw.RZvkViPu-VmHsrPLuUnn-TVjHTI')
