import discord
from discord.ext import commands, tasks
from itertools import cycle
import time
import sys

#client = discord.Client()
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
TOKEN = ''

@client.event
async def on_ready():
    game = discord.Game("Recruiting cracked players like you!")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("Bot online")

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0xF47FFF, title='Fin-S Recruitng', description = f'Welcome to the Fin-S grind {member} and soon enough the Fin-S Family!')
    embed.add_field(name="**What do we offer?**", value="Fortnite, COD, Siege & MTGA Competitions!", inline=False)
    embed.add_field(name="**Socials**", value="Stay updated with the latest news from us by following our Instagram! https://instagram.com/fins.gaming", inline=False)
    embed.add_field(name="**Help & Support**", value="Please alert a staff member of any issues you have", inline=False)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/672169078751887365/753687344585900112/image0-61.png?width=466&height=466')
    embed.set_footer(text="#FINSTFUP")
    await member.send(embed=embed)

# @client.event
# async def on_raw_reaction_add(payload):
#     channel = client.get_channel(payload.channel_id) # Get's the channel where the reaction was added
#     message = await channel.fetch_message(payload.message_id) # Fetches the message to get reactors (API call)
#     reactors = await message.reactions[0].users().flatten() # Makes reactors a list
#     if (client.user in reactors): # Checks if bot is in reactors
#         member = await channel.guild.fetch_member(payload.user_id) # gets the member to add the Verified role
#         role = discord.utils.get(channel.guild.roles, name='Verified') # gets the role
#         await member.add_roles(role) # adds the role

@client.command(aliases = ['h'])
async def Help(ctx):
    embed = discord.Embed(colour=0xF47FFF, title='Help Menu', description='An available list of commands')
    embed.add_field(name='Commands:', value='**-h** \n Displays this help menu \n **-req** \n Shows the competitive team requirements \n **-inv** \n Generates an invite link to the discord')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/672169078751887365/753687344585900112/image0-61.png?width=466&height=466')
    await ctx.send(embed=embed)

@client.command(aliases = ['v']) # Verification message
@commands.has_permissions(administrator=True)
async def verify(ctx):
    embed = discord.Embed(colour=0xF47FFF, title='Verification:', description="You must react to this message to gain access to the server! This verifies that you aren't just a bot")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/672169078751887365/753687344585900112/image0-61.png?width=466&height=466')
    emoji = '<:fins:758721981246996491>'
    message = await ctx.send(embed=embed)
    await message.add_reaction(emoji)

    # async def on_raw_reaction_add():
    #     guild_id = payload.guild_id
    #     guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    #     if payload.emoji.name == 'fins':
    #         role = discord.utils.get(guild.roles, name='Verified')

@client.command(aliases = ['rr']) # Reaction roles
@commands.has_permissions(administrator=True)
async def reactionroles(ctx):
    embed = discord.Embed(colour=0xF47FFF, title='**Reaction Roles:**', description="React and tell us a bit more about yourself!")
    embed.add_field(name='**Roles**', value=f'<:Fortnite:759580618798792734> Fornite <:Fortnite:759580618798792734> \n <:cod:759577654524772392> CallOfDuty <:cod:759577654524772392> \n <:Siege:759582763883298857> Siege <:Siege:759582763883298857> \n <:MTGA:759585244877422632> MTGA <:MTGA:759585244877422632> \n <:OW2:759585717801975830> Overwatch 2 (Soon) <:OW2:759585717801975830>', inline=False)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/672169078751887365/753687344585900112/image0-61.png?width=466&height=466')
    embed.set_footer(text="#FINSTFUP")
    fn = '<:Fortnite:759580618798792734>'
    cod = '<:cod:759577654524772392>'
    siege = '<:Siege:759582763883298857>'
    mtg = '<:MTGA:759585244877422632>'
    ow = '<:OW2:759585717801975830>'
    message = await ctx.send(embed=embed)
    await message.add_reaction(fn)
    await message.add_reaction(cod)
    await message.add_reaction(siege)
    await message.add_reaction(mtg)
    await message.add_reaction(ow)

@client.command(aliases = ['req'])
async def requirements(ctx):
    await ctx.send(f'**Fortnite** \n 200+ PR Points, 2FA Enabled, and tournament experience \n **COD** \n To be determined \n **Siege** \n Diamond or Platinum and competitive experience (Tournament wise) \n **MTGA** \n Mythic Arena on any one format')

@client.command(aliases = ['inv'])
async def invite(ctx):
    invite = await ctx.channel.create_invite(max_age = 300)
    await ctx.send(invite)

client.run(TOKEN)
