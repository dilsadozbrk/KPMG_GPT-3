from flask import Flask, request
import json
import os
from kpmg import storytelling_ai, idea_fn, idea_generation, extract_last_sentence

app = Flask(__name__)

@app.route('/story', methods=['POST'])
def get_story():

    data = request.get_json()
    print(data)

    if all (k in data for k in ("charecter", "scenario", "challenge")):
        character = data['charecter']
        scenario = data['scenario']
        challenge = data['challenge']
        story = storytelling_ai(character,scenario,challenge)
        wmb_gpt3 = extract_last_sentence(story)
        return {"story":story, 
                "question": wmb_gpt3} 

    elif all (k in data for k in ("idea1","idea2", "idea3","GPT3-hmwq")):
        idea1 = data['idea1']
        idea2 = data['idea2']
        idea3 = data['idea3']
        gpt3_hmwq = data['GPT3-hmwq']
        end_story = idea_fn(gpt3_hmwq,idea1,idea2,idea3)
        return {'end_story': end_story}
    
    elif all (k in data for k in ("Original","hmw", "idea11", "idea22", "idea33")):
        ideas = {}
        count = 1
        original_HMWQ = data['Original']
        hmwgpt3 = data['hmw']
        idea1 = data['idea11']
        idea2 = data['idea22']
        idea3 = data['idea33']

        generated_ideas = idea_generation(original_HMWQ, hmwgpt3, idea1,idea2,idea3)
        listofideas = generated_ideas.split('.')
        for idea in listofideas:
            ideas[f"idea{count}"] = idea
            count +=1
        return ideas

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", threaded=True, port=port)

  
