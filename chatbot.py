# chatbot.py - Simple rule-based chatbot

def get_reply(user_input):
    """Return a reply based on the user's input."""
    # Convert input to lowercase to make matching case-insensitive
    user_input = user_input.lower()
    
    # Rule matching using if-elif-else
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def main():
    """Main loop to chat with the user."""
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Get the reply using the function
        reply = get_reply(user_input)
        print("Chatbot:", reply)
        
        # Exit condition: if user said "bye", break the loop
        if user_input.lower() == "bye":
            break

# Run the program only if this script is executed directly
if __name__ == "__main__":
    main()