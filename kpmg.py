import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def extract_last_sentence(string):
    """Function that takes in string and returns the last sentence"""

    sentences = string.split('.')

    return sentences[-1]

def storytelling_ai(character, scenario, challenge):
    """Function that handels GPT3 API calls"""

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Human: Write a story about Marlin in the sea whose challenge is to find his lost son Nemo.\
            \\n\nAI: Story:\n1. Once upon a time, there was a widowed fish, named Marlin, who was extremely protective of his only son, Nemo.\
            \n2. Every day Marlin warned Nemo of the ocean’s dangers and implored him not to swim far away.\
            \n3. One day in an act of defiance, Nemo ignores his father’s warnings and swims into the open water.\
            \n4. Because of that he is captured by a diver and ends up in the fish tank of a dentist in Sydney.\
            \n5. Questions, How might we help Marlin and Nemo find each other? \
            \n##\nHuman: write a story about 2 cells in  human's body whose challenge is to protect the human body from bacteria:\
            \nAI: Story:\
            \n1. ONCE UPON A TIME: There lived 2 cells wondering in a human's body. Their goal was to protect the human body from bacteria.\
            \n2. EVERYDAY: The 2 cells controls the body of the human. (What to do,What to say,What to eat,What to think etc.)\
            \n3. ONE DAY: The Human had an open wound which means the skin was opened and bacteria is free to enter.\
            \n4. BECAUSE OF THAT: The 2 cells have to beat the bacteria by putting them in to the stomach which is full of acid that is to harmful and can Cause Death.\
            \n5. Questions, How might we help the cells beat the bacteria?\
            \n##\nHuman: write a story about a galaxy far far a way in the universe whose challenge is to escape war : \
            \nAI: Story: \
            \n1. ONCE UPON A TIME: There was a galaxy far far away. It was a beautiful place, full of stars and planets.\
            \n2. EVERYDAY: The people of the galaxy lived their lives, going about their business.\
            \n3. ONE DAY: A strange object appeared in the sky. It was a huge ship, and it was heading straight for the planet.\
            \n4. BECAUSE OF THAT: The people of the planet were very afraid. They had never seen anything like it before.\
            \n5. Questions, How might we help the people of the planet when the ship arrives? \
            \n##\nHuman: Write a story about a {character} in {scenario} whose challenge was to {challenge}.\
            \nAI: Story: ",
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Human:", "AI:", "##"]
        )

    # checking the response from the Gpt3 call
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Type error to handle'
    else:
        answer = 'Type error to handle'
    
    return answer

    #HMW = extract_last_sentence(answer)
def idea_fn(hmw,idea1,idea2,idea3):


    
    response2 = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"AI: Questions, How might we help Marlin and Nemo find each other?\
            \nHuman:  1. We tell Marlin to get help from other fishes, \
            \n2. we tell Marlin to talk to Nemo's friends\n3. we tell Marlin to trust Nemo.\
            \n\nAI: Story continues:\
            \n6. Because of that Marlin sets off on a journey to recover Nemo, enlisting the help of other sea creatures along the way.\
            \n7. Until finally Marlin and Nemo find each other, reunite and learn that love depends on trust. \
            \n##\nAI: Questions, How might we help the cells beat the bacteria? \
            \nHuman:  1 we tell the human to go to hospital\
            \n2. we tell the human to eat good food\n3. we tell the human to drink alcohol\
            \n\nAI: Story continues:\
            \n6. BECAUSE OF THAT:  the 2 cells gotten stronger and fought hard\
            \n7. Until finally they defeated the bacteria and saved the human from death. \
            \n##\nAI: Questions, How might we help the people of the planet when the ship arrives? \
            \nHuman:  1 we tell the the people of the planet to wave white flag\
            \n2. we tell the people of the planet to prepare a red carpet\
            \n3. we tell the people of the planet to help each other and stay strong\
            \n\nAI: Story continues:\
            \n6. BECAUSE OF THAT:  the people of the planet got ride of war with the huge ship\
            \n7. Until finally the huge ship peacefully left the planet. \
            \n##\nAI: {hmw}\
            \nHuman:  {idea1}\n{idea2}\n{idea3}\n\nAI: Story continues:\n",
        temperature=0.91,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Human:", "AI:", "##"]
        )

    # checking the response from the Gpt3 call
    if 'choices' in response2:
        if len(response2['choices']) > 0:
            answer2 = response2['choices'][0]['text']
        else:
            answer2 = 'Type error to handle'
    else:
        answer2 = 'Type error to handle'

    return answer2

def idea_generation(hmw,idea1,idea2,idea3,original_HMW):
    response3 = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"AI:  expert in the filed of idea generation, takes as example the following sentence and produces 10 ideas from the question\
            \n\nQuestions, How might we help Marlin and Nemo find each other?\
            \nAI: 1: We tell Marlin to get help from other fishes.\
            \nAI: 2: we tell Marlin to talk to Nemo's friends.\
            \nAI: 3: we tell Marlin to trust Nemo.\
            \n\nQuestions, How might we help the cells beat the bacteria? \
            \nAI: 1: we tell the human to go to hospital.\
            \\nAI: 2: we tell the human to eat good food.\
            \\n\nAI: 3: we tell the human to drink alcohol.\
            \n\nQuestions, How might we help the people of the planet when the ship arrives? \
            \nAI: 1: we tell the the people of the planet to wave white flag.\
            \nAI: 2: we tell the people of the planet to prepare a red carpet.\
            \nAI: 3: we tell the people of the planet to help each other and stay strong.\
            \n\n{hmw} \nAI: 1: {idea1}. \nAI: 2: {idea2}. \nAI: 3: {idea3}. \
            \n\nQuestions, {original_HMW}?\n\nAI:",
        temperature=1,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    # checking the response from the Gpt3 call
    if 'choices' in response3:
        if len(response3['choices']) > 0:
            answer3 = response3['choices'][0]['text']
        else:
            answer3 = 'Type error to handle'
    else:
        answer3 = 'Type error to handle'

    return answer3
