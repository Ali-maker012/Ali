# Define the chatbot function
def chatbot():
    # Take user input
    user_input = input("You: ").lower()
    
    # Base case: Exit if the user types any of the exit words
    exit_words = ["exit", "bye", "quit"]
    if user_input in exit_words:
        print("Chatbot: Goodbye! Have a great day!")
        return  # Stop the chatbot

    # Recursive case: Generate a response and continue the conversation
    print("Chatbot:", response(user_input))  # Generate a response using the response function
    chatbot()  # Recursively call the chatbot function to continue

# Define the response function
def response(user_input):
    # Basic responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "help" in user_input:

