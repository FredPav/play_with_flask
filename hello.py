from flask import Flask
import telegramApi as TA
# insert at 1, 0 is the script path (or '' in REPL)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/telegram-<text>')
def telegram(text):
    TA.callTelegram(text)
    return "sent " + text

@app.route('/welcome-<name>')
def welcomeUser(name):
    return 'Welcome '+name
