
from cgi import print_arguments
from discord.ext import commands
from discord.utils import get

def writeToFile(path,values):
    file = open(path, 'r+')
    FileRead = file.readlines()
    oriFile = []
    for i in FileRead:
        stripLine = i.strip('\n')
        oriFile.append(stripLine)
    oriFile.append(values)
    file.truncate(0)
    for l in oriFile:
        file.write(l+'\n')
    file.close()
bot = commands.Bot(command_prefix='/')

@bot.command()
async def bounce(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def addRoulette(ctx, *args):
    path = r"C:\Users\timot\DiscordBot\Roullette.txt"
    arguments = ' '.join(args)
    print(arguments)
    writeToFile(path, arguments)

bot.run('MTAxOTE3MzM4NjUwNjc0MzgyOA.Gy8JsA.ZVa9ZgT6B40p32ZPBC_cty0bXYjGArMPSCYJ9k')
