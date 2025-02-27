import discord

TOKEN = "YOUR_BOT_TOKEN"
CUSTOM_PHRASE = " @Kubo"  # Change this to your desired text

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        # Ignore bot messages to prevent loops
        if message.author.bot:
            return

        # Debug: Print original message content (text of the message)
        print(f"Original Message: {message.content}")

        # Construct modified message
        content = message.content.strip()
        if content.endswith("."):
            new_content = content[:-1] + CUSTOM_PHRASE
        else:
            new_content = content + CUSTOM_PHRASE

        # Debug: Print modified message
        print(f"Modified Message: {new_content}")

        # Send modified message first, then delete original message
        try:
            # Send the modified message
            await message.channel.send(f"{message.author.mention}: {new_content}")  
            # Delete the original message
            await message.delete()  
        except discord.Forbidden:
            print("Bot lacks permission to manage messages.")
        except discord.HTTPException:
            print("Failed to delete/send message.")

intents = discord.Intents.default()
intents.messages = True  # Ensure message intent is enabled
intents.message_content = True  # Ensure message content intent is enabled

bot = MyBot(intents=intents)
bot.run(TOKEN)
