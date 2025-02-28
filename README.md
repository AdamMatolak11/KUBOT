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
- It edits user messages in real-time.
- Ignores messages from other bots.
- Requires "Manage Messages" permission.

## 📜 License
This project is licensed under the MIT License.

---

### 💡 Need Help?
If you encounter issues, feel free to open an issue in this repository!

