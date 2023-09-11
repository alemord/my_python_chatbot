import spacy
import random

# Load the English language model from spaCy
nlp = spacy.load('en_core_web_sm')

# Define a dictionary of responses based on user intents
responses = {
    'greeting': ["Hello!", "Hi there!", "Hey!"],
    'how_are_you': ["I am good, thank you!", "I am doing well. How about you?"],
    'name': ["I am a chatbot. You can call me Chattona."],
    'goodbye': ["Goodbye!", "See you later!", "Bye!"],
    'ask_weather': ["I'm not sure about the weather. You can check a weather website or app for that information."],
    'ask_time': ["I don't have access to real-time data, but your device's clock can tell you the current time."],
    'ask_joke': ["Sure, here's a joke: Why did the computer keep freezing? Because it left its Windows open!"],
    'ask_age': ["I'm just a computer program, so I don't have an age."],
    'ask_location': ["I exist in the digital realm, so I don't have a physical location."],
    'compliment': ["Thank you! You're pretty awesome too!", "You're making me blush! Thanks!"],
    'insult': ["I'm just a chatbot, there's no need for insults.", "I'm here to help, so let's keep the conversation positive!"],
    'default': ["I'm not sure I understand.", "Could you please rephrase that?", "I apologize, but I am not able to assist with that."],
}

# Define a function to classify user input and return an intent
def classify_intent(user_input):
    doc = nlp(user_input)
    intent = None

    for token in doc:
        if token.text.lower() in ['hello', 'hi', 'hey']:
            intent = 'greeting'
        elif token.text.lower() in ['how', 'are', 'you']:
            intent = 'how_are_you'
        elif token.text.lower() in ['name', 'your']:
            intent = 'name'
        elif token.text.lower() in ['bye', 'goodbye']:
            intent = 'goodbye'
        elif token.text.lower() in ['weather', 'forecast']:
            intent = 'ask_weather'
        elif token.text.lower() in ['time', 'clock']:
            intent = 'ask_time'
        elif token.text.lower() in ['joke', 'funny']:
            intent = 'ask_joke'
        elif token.text.lower() in ['age', 'old']:
            intent = 'ask_age'
        elif token.text.lower() in ['location', 'where']:
            intent = 'ask_location'
        elif token.text.lower() in ['good', 'great', 'awesome']:
            intent = 'compliment'
        elif token.text.lower() in ['bad', 'terrible', 'awful']:
            intent = 'insult'

    return intent


# Start a conversation with the chatbot
print("Chatbot: Hello! How can I help you today? (type 'exit' to end)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    intent = classify_intent(user_input)
    response = responses.get(intent, responses['default'])
    print("Chatbot:", random.choice(response))
