import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# User registration and profile creation
class User:
    def __init__(self, username, age, gender, concerns):
        self.username = username
        self.age = age
        self.gender = gender
        self.concerns = concerns

    def display_profile(self):
        print("Username:", self.username)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Concerns:", ", ".join(self.concerns))


# Chatbot function
def chatbot(user):
    # Greet the user
    print("Hello,", user.username)

    # Ask a question
    print("How are you feeling today?")

    # Get user input
    user_input = input().lower()

    # Tokenize user input
    doc = nlp(user_input)

    # Check user input for different feelings
    if any(token.text in ["good", "great", "happy"] for token in doc):
        print("That's great to hear!")
    elif any(token.text in ["bad", "not", "well", "sad"] for token in doc):
        print("I'm sorry to hear that. How can I assist you today?")
        process_user_concerns(user.concerns)
    else:
        print("I see. How can I assist you today?")
        process_user_concerns(user.concerns)


# Process user concerns
def process_user_concerns(concerns):
    print("Please select from the following options:")
    print("1. Coping strategies")
    print("2. Resources and support")
    option = input()

    if option == "1":
        provide_coping_strategies(concerns)
    elif option == "2":
        provide_resources(concerns)
    else:
        print("Invalid option. Please try again.")


# Provide coping strategies based on user concerns
def provide_coping_strategies(concerns):
    print("Here are some coping strategies based on your concerns:")
    for concern in concerns:
        if concern == "anxiety":
            print("- Practice deep breathing exercises")
            print("- Engage in regular physical activity")
        elif concern == "stress":
            print("- Practice relaxation techniques, such as meditation or mindfulness")
            print("- Prioritize self-care activities")
        # Add more coping strategies for other concerns


# Provide mental health resources based on user concerns
def provide_resources(concerns):
    print("Here are some mental health resources for your concerns:")
    for concern in concerns:
        if concern == "depression":
            print("- National Suicide Prevention Lifeline: 1-800-273-TALK")
            print("- Online support group: www.depressionforums.org")
        elif concern == "substance abuse":
            print("- Substance Abuse and Mental Health Services Administration (SAMHSA): 1-800-662-HELP")
            print("- Local Alcoholics Anonymous (AA) meetings: www.aa.org")
        # Add more mental health resources for other concerns


# Registration process
def register_user():
    print("Welcome! Please provide the following information to create your profile:")
    username = input("Username: ")
    age = input("Age: ")
    gender = input("Gender: ")
    concerns = input("Enter your primary mental health concerns (comma-separated): ").split(",")

    # Create user profile
    user = User(username, age, gender, concerns)

    # Display user profile
    print("\nUser Profile created successfully!")
    user.display_profile()

    # Start chatbot
    chatbot(user)


# Run registration process
register_user()
