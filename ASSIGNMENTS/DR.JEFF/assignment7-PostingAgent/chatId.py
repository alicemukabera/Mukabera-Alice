import requests

BOT_TOKEN = '7617627646:AAE_a2sftEz5tWsY5RZUtbbvz_wnkmmLkt8'

# Get updates sent to the bot
url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()

# Print chat IDs from incoming messages
for update in data['result']:
    print("Chat ID:", update['message']['chat']['id'])
    print("Chat Type:", update['message']['chat']['type'])
    print("Username:", update['message']['chat'].get('username'))
