# Discord Message Modifier Bot

A simple Discord bot that modifies the end of every message in a server by replacing the final period (`.`) with a @Kubo phrase. If a message does not end with a period, the phrase is appended automatically.

## 🚀 Features
- Replaces the ending period (`.`) with a @Kubo phrase.
- Appends the phrase if no period is found at the end.
- Ignores messages from bots to prevent loops.
- Works across all text channels.

## 📦 Requirements
- Python 3.8+
- `discord.py` library

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AdamMatolak11/KUBO_bot.git
   cd KUBO_bot
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

