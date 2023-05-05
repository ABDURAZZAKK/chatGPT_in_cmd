import openai 
import json

openai.api_key = ''


while True:
    req1 = {
        "model": "text-davinci-003",
        "prompt": 'input()',
        "temperature": 0.5,
        "max_tokens": 2000,
        "top_p": 1.0,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.0,}

    req = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role":"user", "content": input()}]
    }

    response = openai.ChatCompletion.create(**req)
    print(json.loads(json.dumps(response))['choices'][0]['message']['content'])