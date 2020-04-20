import keep_alive
import discord
from discord.ext import commands
import json

with open("credentials.json") as creds:
    creds = json.loads(creds.read())
    TOKEN = creds["TOKEN"]  

tierlist_link = 'https://mha-smashrising.github.io/tierlist/'
calculate_link = 'https://mha-smashrising.github.io/tierlist/calculator.html'
github_link = 'https://github.com/mha-smashrising/'

client = discord.Client()

class Bot(commands.Bot):
    def __init__(self):
        super(Bot, self).__init__(command_prefix="$", case_insensitive=True)
        self.pool = None

bot = Bot()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    # print(bot.user.id)
    print('------')


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$tierlist'):
#         await message.channel.send('https://github.com/mha-smashrising/tierlist')

# About Command
@bot.command()
async def about(ctx):
    aboutEmbed = discord.Embed(
        title="A discord.py bot for Smash Rising Discord Server",
        # description="Type ``%s`` for a list of available commands\n__\n__" % "o!help",
        color=0xD800FF
    )
    aboutEmbed.set_author(name=bot.user.name + ' - About', icon_url=bot.user.avatar_url)
    aboutEmbed.set_thumbnail(url=bot.user.avatar_url)
    aboutEmbed.add_field(name="Written By", value=(await bot.application_info()).owner.mention)
    # aboutEmbed.add_field(name="Version", value=ver, inline=False)
    aboutEmbed.add_field(name="Git Repository", value=github_link)
    # aboutEmbed.add_field(name="Contributor(s)", value=f"{bot.get_user(119149398306455552).mention} - Data Collection")
    await ctx.send(embed=aboutEmbed)

# tierlist
@bot.command()
async def tierlist(ctx):
    # await ctx.send(arg + " <-- this means the bot is online.. nya >.<")
    await ctx.send('NOTE: This is not a comprehensive tier list, just a ranking based on how much power each card gives in terms of their stats.\n' + tierlist_link)

# calculate
@bot.command()
async def calculate(ctx):
    await ctx.send(calculate_link)

keep_alive.keep_alive()

bot.run(TOKEN)

