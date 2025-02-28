# Discord Message Modifier Bot

A simple Discord bot that modifies the end of every message in a server by replacing the final period (`.`) with a @Kubo phrase. If a message does not end with a period, the phrase is appended automatically.

## 🚀 Features
- **Message Modification**: Replaces the ending period (`.`) with a `@Kubo` mention or appends it if no period is found.
- **Bot Management**: Slash commands to activate and deactivate the bot (only for the bot owner).
- **Bot Stats**: Shows the bot’s uptime and message count.
- **Real-time Updates**: The bot processes and modifies messages in real-time.
- **Bot Permission Management**: Ensure the bot has the necessary permissions to manage messages and interact with users.

## 📦 Requirements
- Python 3.8+
- `discord.py` library

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AdamMatolak11/KUBOT.git
   cd KUBOT
   ```
2. Install dependencies:
   ```bash
   pip install discord
   ```
3. Replace `YOUR_BOT_TOKEN` in `bot.py` with your actual Discord bot token.

## ▶️ Usage
Run the bot using:
```bash
python bot.py
```

## 🛠 Bot Permissions
Ensure your bot has the following permissions:
- "Manage Messages" (to edit messages)
- "Read Messages" & "Send Messages" (basic functionality)
- "Use Slash Commands" (for command execution)

## ⚙️ Configuration
Modify `@Kubo` in `bot.py` to change the appended phrase.
```python
CUSTOM_PHRASE = " @Kubo"  # Change this to your desired text
```

## 📝 Example
| Input        | Output                |
|-------------|------------------------|
| `Hello world.` | `Hello world @Kubo` |
| `Hello world`  | `Hello world @Kubo` |

## 🤖 Bot Behavior
- Message Editing: The bot edits user messages by adding the custom mention at the end of the message.
- Real-time Processing: It processes messages as they are sent in the channel.
- Bot Management: The bot can be activated or deactivated using slash commands (/kubon, /kuboff).
- Stats: Use /stats to view the bot's uptime and message processing stats.

## 🧑‍💻 Slash Commands
/kubon
- Description: Activates the bot (only for the bot owner).
- Usage: /kubon
- Permission: Only the bot owner can use this command.
/kuboff
- Description: Deactivates the bot (only for the bot owner).
- Usage: /kuboff
- Permission: Only the bot owner can use this command.
/status
- Description: Displays whether the bot is active or inactive.
- Usage: /status
- Permission: Anyone can use this command.
/stats
- Description: Shows the bot’s stats, including message count and uptime.
- Usage: /stats
- Permission: Anyone can use this command.

## 📜 License
This project is licensed under the MIT License.

---

### 💡 Need Help?
If you encounter issues, feel free to open an issue in this repository!

