# Chatbot
Created Chatbot Using Python &amp;

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
