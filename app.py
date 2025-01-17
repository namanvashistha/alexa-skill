from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")  # The endpoint for Alexa to interact with your app


# LaunchRequest handler
@ask.launch
def launch_skill():
    welcome_message = "Welcome to my Raspberry Pi Alexa Skill! How can I assist you?"
    return question(welcome_message)


# IntentRequest handler
@ask.intent("HelloIntent")
def hello_intent():
    return statement("Hello! It's great to talk to you from Raspberry Pi.")


@ask.intent("GoodbyeIntent")
def goodbye_intent():
    return statement("Goodbye! Have a great day.")


# Session Ended handler
@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
