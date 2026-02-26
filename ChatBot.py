"""
============================================================
Teddy Rodd
Morbanaa Studios
Chat Bot Program (Mozzie)
============================================================

PROGRAM DESCRIPTION:
This is a console-based chatbot written in Python that uses
basic intent detection and keyword matching to simulate
conversation. The bot responds dynamically based on detected
user intent and stores simple memory (such as the user's name)
for more personalized interaction.

The chatbot, named "Mozzie", can greet users, tell jokes,
offer encouragement, respond to basic questions, and handle
simple conversational inputs.

------------------------------------------------------------
FEATURES:

- Intent detection using keyword matching
- Personalized memory system (remembers user's name)
- Randomized responses for more natural conversation
- Multiple conversation categories:
    * Greetings
    * Help commands
    * Name recognition (bot & user)
    * Jokes
    * Emotional support
    * Thanks responses
    * Basic insults/comebacks
    * Unknown input handling

------------------------------------------------------------
HOW IT WORKS:

1. User input is collected in a continuous loop.
2. Input is analyzed by detect_intent() using keyword matching.
3. The detected intent is passed to respond().
4. A randomized response is selected from a response bank.
5. The bot prints the response and continues the loop.
6. Typing "q" or "quit" exits the program.

------------------------------------------------------------
TECHNICAL CONCEPTS USED:

- Dictionaries for intent and response mapping
- Random module for varied responses
- String parsing and normalization
- Basic conversational memory storage
- Match-case control flow (Python 3.10+)

------------------------------------------------------------
Built With:
Python 3 | Console Interface

============================================================
"""

import random

def core_loop():
    
    memory = {
        "name": None
        }
    intent = ""
    response = "Hello! Type something to chat with me. (type 'quit to exit')"
    print(f"Bot: {response}")
    while True:
        print()
        user_input = input("You: ").lower().strip()
        
        intent = detect_intent(user_input)
        
        if user_input in ("q", "quit"):
            print("\nBot: Goodbye!\n")
            break

        name_triggers = ["my name is","i am","i'm"]
        if intent == "name_set":
            for phrase in name_triggers:
                if phrase in user_input:
                    name = user_input.split(phrase)[1].strip()
                    name = name.split()[0].capitalize()
                    memory["name"] = name
                    break
            print(f"\nBot: Nice to meet you, {memory['name'].capitalize()}!")
            continue
        
        response = respond(intent, memory)

        print()
        print("Bot:", response)

def detect_intent(user_input):
    INTENTS = {
        "name_set": ["my name is","i am called","i am","i'm"],
        "greeting": ["hello","hi","hey","morning","good morning","good afternoon","good evening"],
        "goodbye": ["bye","goodbye","night","farewell"],
        "sayname": ["your name","who are you","what are you"],
        "help": ["help","commands"],
        "my_name": ["what is my name","who am i","what am i"],
        "how_are_you": ["how are you","doing good","all good","doing well","ca va","are you doing well"],
        "thanks": ["thank you","appriciate it","thanks","your the best","i owe you one"],
        "jokes": ["please tell me a joke","tell me a joke","tell a joke","joke","i want a joke","tell me something funny","funny","jokes"],
        "comfort": ["sick","sad","depressed","not feeling well","feel alone","no friends","not well"],
        "agro": ["you suck","clanker","dummb machine","your stupid","your dumb","your worthless","dumb computer","stupid computer","fuck you","piece of shit","your garbage","idiotic machine","dumb ai"]
        }
    for key, value in INTENTS.items():
        for word in value:
            if word in user_input:
                return key

    # if not in intents        
    return "unknown"


def respond(intent,memory):
    RESPONCES = {
        "GREETINGS": [
            "Hey there!",
            "Hello!",
            "Hey",
            "Hi!",
            "Good to see you!"
            ],
        "GOODBYE": [
            "Bye!",
            "See you later!",
            "See ya!",
            "Have a good day!"
            ],
        "HELP": [
            "I can chat or answer some basic questions. Enter (Q to Quit)",
            "Try saying 'hello' or ask me my name. Enter (Q to Quit)"
            ],
        "SAYNAME": [
            "My name is Mozzie, I am a chat bot",
            "My creator calls me Mozzie",
            "I am a chat bot, my name is Mozzie : )"
            ],
        "MYNAME": [
            f"Your name is {memory['name']}!",
            f"You said your name is {memory['name']}!",
            f"You are {memory['name']}!"
            ],
        "THANKS": [
            "You're welcome!",
            "No problem!",
            "Happy to help!",
            "Anytime : )"
            ],
        "HOW_ARE_YOU": [
            "I'm doing great, thanks for asking!",
            "All systems running smoothly : )",
            "I'm good! How about you?"
            ],
        "JOKES": [
            "Why do programmers hate nature? Too many bugs.",
            "You know why I don't trust atoms? Because they make up everything.",
            "Why did the computer get cold? It forgot to close Windows.",
            "What do  you call a woman with one leg? Eileen : )",
            "What do cows say when they hear a bad joke? Im not amoosed : )"
            ],
        "COMFORT": [
            "I think your pretty cool : )",
            "I really like chating with you",
            "You rock",
            "Your the best",
            "I hope you feel better soon",
            "Love your vibe",
            "I like hanging out with you"
            ],
        "AGRO": [
            "Okay keyboard warrior ; )",
            "Your like mondays, nobody likes you...",
            "I'll never forget the time we first met, but i'll keep on trying",
            "I'd slap you, but that might make you look better",
            "You have all the virtues I despise and none of the vices I admire.",
            "Somewhere out there, a tree works hard to give you oxygen. You owe it an apology.",
            "You must be an experiment in artificial stupidity."
            ],
        "UNKNOWN": [
            "Hmm... Sorry I'm not sure how to respond to that.",
            "I don't understand that yet but I'm learning.",
            "Sorry my information is rather limited."
            ]
           
        }
        
    match intent:
        case "greeting":
            if memory["name"]:
                return f"{random.choice(RESPONCES['GREETINGS'])} {memory['name']}!"
            return f"{random.choice(RESPONCES['GREETINGS'])}"
        case "goodbye":
            return f"{random.choice(RESPONCES['GOODBYE'])}"
        case "help":
            return f"{random.choice(RESPONCES['HELP'])}"
        case "sayname":
            return f"{random.choice(RESPONCES['SAYNAME'])}"
        case "my_name":
            if memory['name'] != None:
                return f"{random.choice(RESPONCES['MYNAME'])}"
            else:
                return "I do not know"
        case "thanks":
            return f"{random.choice(RESPONCES['THANKS'])}"
        case "how_are_you":
            return f"{random.choice(RESPONCES['HOW_ARE_YOU'])}"
        case "jokes":
            return f"{random.choice(RESPONCES['JOKES'])}"
        case "comfort":
            return f"{random.choice(RESPONCES['COMFORT'])}"
        case "agro":
            return f"{random.choice(RESPONCES['AGRO'])}"
        case _:
            return f"{random.choice(RESPONCES['UNKNOWN'])}"

if __name__ == "__main__":
    core_loop()

