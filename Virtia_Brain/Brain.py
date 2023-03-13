from Class.TwitchChat import TwitchChat
from Class.OpenAI_API import OpenAI_API
import time


chat = TwitchChat("poseydon989", "oauth:YOUR_AUTH", "poseydon989")
openai_api = OpenAI_API()
BotList = ["Moobot", "Nightbot", "StreamElements", "Streamlabs", "Virtia"]


def main():
    while True:
        # read chat messages and print them continuously
        queue = time.time()
        for username, channel, message in chat.read_chat():
            print(f"{username}: {message}")
            # check if username lowercased is in the bot list lowercased, then continue
            if username.lower() in [bot.lower() for bot in BotList]:
                continue
            # check if the message is a command, emoji or link, then continue
            if message.startswith("!") or message.startswith(":") or "http" in message:
                continue
            # check if it's been more than 30 seconds since the last message, then continue
            # if time.time() - queue > 30:
            #     print('here3')
            #     continue
            reponse = openai_api.chat(username + ': ' + message)
            chat.write_chat("[Virtia]: " + reponse)
            print(reponse)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()

# Path: Virtia_Brain\Brain.py
