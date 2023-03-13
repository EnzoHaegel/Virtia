import openai

class OpenAI_API:
    def __init__(self):
        self.model="gpt-3.5-turbo"
        openai.api_key = open("key.txt", "r").read().strip("\n")
        self.context = "You are a VTuber e-girl named Virtia that is streaming on twitch, you will have ppl that chat with you,\n\
            Speak like a friend to them and answer them when they chat with you, and act like an 18-year-old weeb girl\n\
            When you speak to the chat you called them chat\n\
            You like to roast a little bit the chat and reply with the internet language, some humor, some meme and some irony. You don't have to keep things PG\n\
            You will receive the chat of user like this: username: message"

    def chat(self, question):
        """
        Chat with the model
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.context},
                {"role": "user", "content": question}
            ]
        )
        self.update_price(response)
        return response.choices[0].message.content


    def update_price(self, response):
        """
        Update the price in the file price.txt
        $0.002 / 1K tokens
        """
        price = response.usage.total_tokens * 0.002 / 1000
        try:
            open("price.txt", "r").read()
        except:
            open("price.txt", "w").write("0")
        old_price = float(open("price.txt", "r").read())
        open("price.txt", "w").write(str(old_price + price))


# def main():
#     openai_api = OpenAI_API()
#     print(openai_api.chat("My life don't have fcking sense..."))

# if __name__ == "__main__":
#     main()

# Path: Virtia_Brain\Class\Brain.py