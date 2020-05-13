import discord
from discord.utils import get
import asyncio

client = discord.Client()
BOT_TOKEN = 'INSERT YOUR BOT TOKEN HERE'
colour_map = {"red": "#FF2D00", "orange": "#FF7B00", "yellow": "#F5CD00", "green": "5EF500", "blue": "0073F5", "purple": "8C00F5", 
              "pink": "F500CD"} #List of basic colours if user inputs with no hex code (Add more if you want)

@client.event
async def on_ready():
    print("Bot is ready") #Prints to terminal to know when bot is active
    await client.change_presence(activity=discord.Game("Bot is ready!")) #Under Bot's name activity will be displayed

@client.event
async def on_message(message): #When someone sends a message on server
    channel = message.channel
    user = message.author
    guild = user.guild

    if user == client.user: #If bot is client of message, will not proceed with rest of code
        return

    if "!help" in message.content: #'colours' is help command that will list all basic supported colours (you can change)
        embed = discord.Embed(title="Commands:", color=0xFF2D00)
        embed.add_field(name="!help", value="Prints this message", inline=False)
        embed.add_field(name="!colour <colour hexcode>",
        value="Assign colours using 6 digit hex codes\nExample Usage: !color #FABCDE\nSee: https://www.google.com/search?q=color+picker", inline=False)
        embed.add_field(name="!colour <colour name>\nCurrent list of colours:", value=str(" \n".join(colour_map.keys())), inline=False)

        await channel.send(content="",embed=embed)

    if "!colour " in message.content : #Main command colour = 
        colour_name = message.content[8::].lower() #After !colour 
        rgb = hex_to_rgb(colour_name) #Converts colour to rgb
        await asyncio.sleep(1)
        if rgb != None: #If hex code was inputted it will enter here
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]

            await assign_colour(user, guild, colour_name, channel,r, g, b)
        else: #If actual colour name was inputted it will enter here (anything not hexcode)
            if colour_name in colour_map:
                colour_name = colour_map[colour_name] #Retrieves the colour's hex code
                rgb = hex_to_rgb(colour_name)
            
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                await assign_colour(user,guild, colour_name, channel,r, g, b) 
            else: #If the text inputted after 'colour = ' is not a valid colour
                embed = discord.Embed(title="", color=0xFF7B00)
                embed.add_field(name="Invalid Colour",value="That colour does not exit in my colour list!\nUse ``!help`` to view the list", inline=False)
                await channel.send(content="",embed=embed)


def hex_to_rgb(colour_hex):
    try:
        colour_name = colour_hex.replace("#", "")
        colour_name = colour_name.strip()
        return(tuple(int(colour_name[i:i+2], 16) for i in (0, 2, 4)))
    except:
        return(None)


async def assign_colour(user, guild, colour_name, channel, r, g, b):
    user_name = user.name
    user_role = get(user.guild.roles, name=user.name)

    if user_role != None: #If the role under user.name has already been created
        await user_role.edit(colour=discord.Colour.from_rgb(r,g,b),position=user.top_role.position) #Edits colour of role

    else: #If role under user.name is not found
        await guild.create_role(name=user_name, colour=discord.Colour.from_rgb(r, g, b))
        await asyncio.sleep(1) #Sleeps to make sure role has been created before retrieving it 
        user_role = get(user.guild.roles, name=user.name) #retrieves created role
        await asyncio.sleep(1)#Ensures the role has been retrieved before editing
        await user_role.edit(position=user.top_role.position) #Moves role to position above highest current role that user has 
        await user.add_roles(user_role) #Adds role to user

    #Feedback to user that the colour has changed
    embed = discord.Embed(title="",colour=discord.Colour.from_rgb(r,g,b))
    embed.add_field(name="Colour Assigned",value=user.mention + " changed colour to **#" + colour_name.replace("#", "") + "**", inline=False)

    await channel.send(content="",embed=embed)

client.run(BOT_TOKEN)
