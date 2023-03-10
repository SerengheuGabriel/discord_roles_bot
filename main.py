import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    # response = f'Hi {member.display_name}, welcome to my Hell!'
    # channel = bot.get_channel(756148810224369756)
    # await channel.send(response)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# @bot.event
# async def on_member_update(before, after):
#     response = f'{before.display_name} is now {after.display_name}. Much wow'
#     channel = bot.get_channel(1037855625729818755)
#     await channel.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.event
# async def on_member_join(member):
#     # response = f'Hi {member.display_name}, welcome to my Hell!'
#     # channel = bot.get_channel(756148810224369756)
#     # await channel.send(response)
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@bot.event
async def on_member_remove(member):
    response = f"Everybody say peepo bye {member.display_name} 👋!"
    channel = bot.get_channel(756148810224369756)
    await channel.send(response)


@bot.event
async def on_member_join(member):
    response = f"Everybody say hi to  {member.display_name} 👋 Please go to the role-picker channel and use " \
               f"?wtf to see role options!"
    channel = bot.get_channel(756148810224369756)
    await channel.send(response)

# @bot.event
# async def on_message(message):
#
#     print(message.author, message.content, message.channel.id)

@bot.command(name="wtf")
async def on_message(message):

    response = f"Thank you for using this bot, brought to you by amish services. " \
               f"Don't worry, they don't know this uses electricity :wink: \n" \
               f"List of commands: \n ?roles - gives a list of roles and role names" \
               f"\n - Use the buttons under ?roles to toggle that role" \
               f"\n ?myRoles - shows a list of all your active roles" \
               f"\n ?requestNewRole - request the addition of a new role for a game or otherwise" \
               f" \n please us the syntax ?requestNewRole newRoleName (Game Title/ purpose of role) \n\n" \
               f"Fuck you."
    await message.channel.send(response)

@bot.command(name="benta")
async def on_message(message):

    response = f"https://tenor.com/view/i-show-speed-speed-shake-now-suck-that-sucking-gif-24039341"
    await message.channel.send(response)


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="1. HOTS", style=discord.ButtonStyle.primary, row=0, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def hots_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[0] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[0])
            response = "Definitely NOT League of Legends (Heroes of the Storm) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[0])
            response = "Definitely NOT League of Legends (Heroes of the Storm) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="2. Zomboid", row=0, style=discord.ButtonStyle.primary,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def zomboid_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[1] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[1])
            response = " Early Access Zombie Survival Gamers (Project: Zomboid) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[1])
            response = " Early Access Zombie Survival Gamers (Project: Zomboid) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="3. BLOONS 6", row=0, style=discord.ButtonStyle.primary,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def bloons_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[2] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[2])
            response = "Sniper Monkeys (BLOONS 6) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[2])
            response = " Sniper Monkeys (BLOONS 6) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="4. PULSAR", row=0, style=discord.ButtonStyle.primary,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def pulsar_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[3] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[3])
            response = "Space Pirates (PULSAR: Lost Colony) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[3])
            response = "Space Pirates (PULSAR: Lost Colony) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="5. ROR 2", row=0, style=discord.ButtonStyle.primary,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def ror2_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[4] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[4])
            response = "101% crit chance (Risk of Rain 2) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[4])
            response = "101% crit chance (Risk of Rain 2) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="6. Tabletop Sim", row=1, style=discord.ButtonStyle.success,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def tabletop_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[5] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[5])
            response = "(╯°□°）╯︵ ┻━┻ Simulator (Tabletop Simulator) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[5])
            response = "(╯°□°）╯︵ ┻━┻ Simulator (Tabletop Simulator) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="7. Sea of Thieves", row=1, style=discord.ButtonStyle.success,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def sea_of_thieves_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[6] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[6])
            response = "Lovers of Booty (Sea of Thieves) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[6])
            response = "Lovers of Booty (Sea of Thieves) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="8. Minecraft", row=1, style=discord.ButtonStyle.success,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def mc_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[7] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[7])
            response = "Blockheads (Minecraft) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[7])
            response = "Blockheads (Minecraft) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="9. Overcooked", row=1, style=discord.ButtonStyle.success,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def overcooked_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[8] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[8])
            response = "Hell's Kitchen Enjoyers (Overcooked 1 or 2) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[8])
            response = "Hell's Kitchen Enjoyers (Overcooked 1 or 2) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="10. The Forest", row=2, style=discord.ButtonStyle.danger,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def forest_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[9] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[9])
            response = "Canibalistic Woodcutters (The Forest) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[9])
            response = "Canibalistic Woodcutters (The Forest) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="11. Hunt Showdown", row=2, style=discord.ButtonStyle.danger,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def hunt_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[10] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[10])
            response = "Crippled Hunters (Hunt: Showdown) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[10])
            response = "Crippled Hunters (Hunt: Showdown) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="12. Dead by Daylight", row=2, style=discord.ButtonStyle.danger,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def dbd_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[11] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[11])
            response = "Shirtless Myres Enjoyers (Dead by Daylight) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[11])
            response = "Shirtless Myres Enjoyers (Dead by Daylight) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="13. Overwatch", row=2, style=discord.ButtonStyle.danger,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def overwatch_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[12] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[12])
            response = "OWO-2 (Overwatch) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[12])
            response = "OWO-2 (Overwatch) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

    @discord.ui.button(label="14. Barotrauma", row=2, style=discord.ButtonStyle.danger,
                       emoji="😎")  # Create a button with the label "😎 Click me!" with color Blurple
    async def barotrauma_button_callback(self, interaction, button):

        guild = bot.get_guild(1037855624278577225)
        rolesArr = []

        for r in guild.roles:
            if (r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                               "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
                rolesArr.append(r)

        if rolesArr[13] in interaction.user.roles:
            await interaction.user.remove_roles(rolesArr[13])
            response = "Baro-Traumatic Experience (Barotrauma) role has been toggled off"
        else:
            await interaction.user.add_roles(rolesArr[13])
            response = "Baro-Traumatic Experience (Barotrauma) role has been toggled on"
        await interaction.response.send_message(response, ephemeral=True)

@bot.command(name="roles")
async def on_message(ctx):

    guild = bot.get_guild(1037855624278577225)

    response = "Available roles for role-picker:\n"
    roles = []

    for r in guild.roles:
        if(r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                          "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
            roles.append(r.name)
            response = response + "-" + str(len(roles)) + ". " + r.name + "\n"
    await ctx.send(response, view=MyView())

@bot.command(name="myRoles")
async def on_message(message):

    guild = bot.get_guild(1037855624278577225)

    response = "Your roles are:\n"
    roles = []

    for r in guild.roles:
        if(r.name not in ["@everyone", "Iraq", "Romania", "USA", "Deutschland", "Penis", "Role picker", "-rep",
                          "Raid Shadow Legends", "Midjourney Bot", "Hydra"]):
            roles.append(r.name)
            if r in message.author.roles:
                response = response + "-" + str(len(roles)) + ". " + r.name + "\n"
    await message.channel.send(response)

@bot.command(name="requestNewRole")
async def on_message(ctx):

    guild = bot.get_guild(1037855624278577225)
    newRole = ctx.message.content.split(" ")
    await guild.get_member(276781784581144577).create_dm()
    await guild.get_member(276781784581144577).dm_channel.send(
        f"I ({ctx.author.name}) would like the new role {newRole[1]}, "
        f"for the purpose of {newRole[2]}, make it now or die!"
    )
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(
        f"You successfully sent the server owner a "
        f"request for the new role {newRole[1]}, for the purpose of {newRole[2]}. Kinda needy but ok"
    )


bot.run(TOKEN)
