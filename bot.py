import discord
from discord import app_commands
from discord.ext import commands
import datetime

TOKEN = "YOUR_BOT_TOKEN"
KUBO_ID = 123456789098765  # Replace with Kubo's actual user ID
BOT_OWNER_ID = 123456789098765  # Replace with your Discord user ID

CUSTOM_PHRASE = f" <@{KUBO_ID}>"  # Space before mention

# Enable intents
intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True  

# Create bot with commands support
bot = commands.Bot(command_prefix="!", intents=intents)

# Track bot activity state
bot.active = True  
bot.message_count = 0  # Track the number of messages

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands
    print(f'Logged in as {bot.user}')
    print("Slash commands synced!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bot messages

    # Ignore messages if the bot is logged out
    if not bot.active:
        return

    # Track message count
    bot.message_count += 1

    # Modify user messages
    content = message.content.strip()
    if content.endswith("."):
        new_content = content[:-1] + CUSTOM_PHRASE
    else:
        new_content = content + CUSTOM_PHRASE

    # Debug prints
    print(f"Original Message: {message.content}")
    print(f"Modified Message: {new_content}")

    try:
        await message.channel.send(f"{message.author.mention}: {new_content}")  
        await message.delete()  
    except discord.Forbidden:
        print("Kubot lacks permission to manage messages.")
    except discord.HTTPException:
        print("Failed to delete/send message.")

# ✅ Slash command for login
@bot.tree.command(name="kubon", description="Activates the Kubot (only for the owner).")
async def login(interaction: discord.Interaction):
    if interaction.user.id == BOT_OWNER_ID:
        bot.active = True
        await interaction.response.send_message("🟢 Kubot is now active (logged in).", ephemeral=True)
    else:
        await interaction.response.send_message("❌ You don’t have permission to log in the Kubot!", ephemeral=True)

# ❌ Slash command for logout
@bot.tree.command(name="kuboff", description="Deactivates the Kubot (only for the owner).")
async def logout(interaction: discord.Interaction):
    if interaction.user.id == BOT_OWNER_ID:
        bot.active = False
        await interaction.response.send_message("🔴 Kubot is now inactive (logged out).", ephemeral=True)
    else:
        await interaction.response.send_message("❌ You don’t have permission to log out the Kubot!", ephemeral=True)

# 🟢 Slash command for bot status
@bot.tree.command(name="status", description="Shows whether the Kubot is active or inactive.")
async def status(interaction: discord.Interaction):
    status = "active" if bot.active else "inactive"
    await interaction.response.send_message(f"The Kubot is currently {status}.", ephemeral=True)

# 🔥 Slash command for bot stats
@bot.tree.command(name="stats", description="Shows the Kubot's stats, like message count.")
async def stats(interaction: discord.Interaction):
    # Get the bot's creation time and the current time in UTC
    created_at = bot.user.created_at.replace(tzinfo=datetime.timezone.utc)
    current_time = datetime.datetime.now(datetime.timezone.utc)

    # Calculate uptime
    uptime = current_time - created_at
    await interaction.response.send_message(f"Kubot Stats:\n"
                                           f"Messages Processed: {bot.message_count}\n"
                                           f"Uptime: {str(uptime).split('.')[0]}", ephemeral=True)

bot.run(TOKEN)
