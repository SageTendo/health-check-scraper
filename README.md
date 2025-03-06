# **Higher Health Check Automation** 🚀 *(Archived)*  

> ⚠️ This project was developed for **personal use** during COVID-19 and is no longer actively maintained.

A script that automates the daily health check process on the government website during COVID-19, using a Telegram bot for interaction. 
Initially, the project included Discord integration, but that feature was a work in progress and has since been removed.

## 💡 Why I Made This  
During university, I was required to submit daily health checks due to COVID-19 protocols. This task became repetitive and time-consuming. To simplify it, I created a Telegram bot that automates the process. With just a text command, I could easily complete the health check every day, saving time and ensuring I didn’t forget to submit it.

## 🛠️ Tech Stack  
- **Language:** Python  
- **Libraries:** `requests`, `BeautifulSoup`, `RoboBrowser` `python-telegram-bot`  
- **Automation:** Web scraping and form submission  

## 📦 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/higher-health-check-automation.git
   cd higher-health-check-automation
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Configure the bot:  
   - Set up your Telegram bot and obtain an API token from [BotFather](https://t.me/botfather).  
   - Update the .env file with your bot token and other required details.  

## 🚀 Usage  
Run the script with:  
```bash
python ./bots/telegram/telegramBot.py
``` 
