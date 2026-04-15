def chatbot():
    print("AI Bot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("AI Bot: Hi there!")
        elif user == "how are you":
            print("AI Bot: I'm doing great!")
        elif user == "your name":
            print("AI Bot: I'm a Python chatbot.")
        elif user == "bye":
            print("AI Bot: Goodbye!")
            break
        else:
            print("AI Bot: I don't understand that.")

chatbot()
