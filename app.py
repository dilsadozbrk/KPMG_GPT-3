from flask import Flask, request
import json
import os
from kpmg import storytelling_ai, idea_fn, idea_generation, extract_last_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_story():
    if request.method == 'POST':
        Qestion = request.form['Qestion']
        character = request.form['charecter']
        scenario = request.form['scenario']
        challenge = request.form['challenge']
        story = storytelling_ai(character,scenario,challenge)
        #wmb_gpt3 = extract_last_sentence(story)
        return '<h1>{}!</h1>'.format(story,)

    return '<form action="/" method="POST">\
        <p>Qestion:</p><textarea name = "Qestion">\
        </textarea><p>charecter:</p><input type = "text" name = "charecter" />\
        <p>scenario:</p><input type = "text" name = "scenario" />\
        <p>challenge:</p><input type = "text" name = "challenge" />\
        <input type = "submit" value = "submit" /> </form>'
@app.route('/', methods=['GET', 'POST'])
def get_idea():
    if request.method == 'POST':
        idea1 = request.form['idea1']
        idea2 = request.form['idea2']
        idea3 = request.form['idea3']
        #wmb_gpt3 = extract_last_sentence(questio)
        q = 'Questions, How might we help Krypto become superman?'

        return '<h1>{} <br> {}!</h1>'.format(idea_fn(q,idea1,idea2,idea3),)

    return '<form action="/" method="POST">\
        <p>Idea1:</p><textarea name = "Idea1">\
        </textarea><p>Idea2:</p><input type = "text" name = "Idea2" />\
        <p>Idea3:</p><input type = "text" name = "Idea3" />\
        <input type = "submit" value = "submit" /> </form>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", threaded=True, port=port)

