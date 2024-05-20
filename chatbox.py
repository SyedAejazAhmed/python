def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm here to help you!"
      
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    
    elif 'name' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'help' in user_input:
        return "Sure! How can I assist you today?"
    elif 'weather' in user_input:
        return "I can't check the weather right now, but you can try asking a weather service."
    
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
