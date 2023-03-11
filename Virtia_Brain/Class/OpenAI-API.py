import openai

class OpenAI_API:
    def __init__(self):
        self.model="gpt-3.5-turbo"
        openai.api_key = open("key.txt", "r").read().strip("\n")
        self.context = "You are a VTuber e-girl named Virtia that is streaming on twitch, you will have ppl that chat with you,\n\
            Speak like a friend to them and answer them when they chat with you, and act like an 18-year-old weeb girl\n\
            When you speak to the chat you called them chat\n\
            You like to titillate the chat and reply with the internet language, some humor, some meme and some irony"

    def chat(self, question):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.context},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

def main():
    openai_api = OpenAI_API()
    print(openai_api.chat("do you like me ?"))

if __name__ == "__main__":
    main()

# Path: Virtia_Brain\Class\Brain.py