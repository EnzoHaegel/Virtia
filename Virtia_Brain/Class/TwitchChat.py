import socket
import re

class TwitchChat:
    def __init__(self, username, token, channel):
        self.username = username
        self.token = token
        self.channel = channel

        # Connect to Twitch IRC server
        self.sock = socket.socket()
        self.sock.connect(("irc.chat.twitch.tv", 6667))
        self.sock.send(f"PASS {self.token}\n".encode("utf-8"))
        self.sock.send(f"NICK {self.username}\n".encode("utf-8"))
        self.sock.send(f"JOIN #{self.channel}\n".encode("utf-8"))

        # Compile regex pattern for extracting message data
        self.message_pattern = re.compile(r":(.*)!(.*)@(.*)\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)")

    def read_chat(self):
        # Receive data from Twitch IRC server
        data = self.sock.recv(2048).decode("utf-8")

        # Split data into separate lines
        lines = data.split("\r\n")

        # Extract message data from each line
        for line in lines:
            match = self.message_pattern.match(line)
            if match:
                username, _, _, channel, message = match.groups()
                yield username, channel, message
    
    def write_chat(self, message):
        # Send message to Twitch IRC server
        self.sock.send(f"PRIVMSG #{self.channel} :{message}\n".encode("utf-8"))

