# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the ChatBot class for interaction.
class ChatBot:
    def __init__(self):
        # Initializing the sentiment analysis tool.
        self.sentiment_analyzer = TextBlob("")
            # Analyzing the sentiment of the user's message.
    def start_chat(self):
        print("Chatbot: Hi, how can I help you today?")
        while True:
            user_message = input("You: ").strip()
            
            # Generating the chatbot's response based on sentiment.
            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            # Printing the chatbot's response and sentiment.
            if(sentiment_score > 0):
                chatbot_message = f"Chatbot: That's great to hear! \n Sentiment Score: {sentiment_score}"
            elif(sentiment_score < 0):
                chatbot_message = f"Chatbot: I'm sorry to hear that. Would you like me to transfer you to a live agent? \n Sentiment Score: {sentiment_score}"
            else:
                chatbot_message = f"Chatbot: I see.\n Sentiment Score: {sentiment_score}"

            print(chatbot_message)

    # Creating the chatbot and starting the chat loop.
if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()