from flask import Flask, render_template
from flask_ask import Ask, statement, question, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome_message = 'Bem vindo ao Meu Busão'
    return statement(welcome_message)

@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)

if __name__ == '__main__':
    app.run(debug=True)