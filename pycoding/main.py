import requests
import json

messages = []
while True:
    msg = input('Write a message: ')
    messages.append({
        'role' : 'user',
        'content' : msg
    })

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>"
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "messages": messages        
    })
    )

    if response.status_code == 200:
        res_dict = response.json()
        messages.append(res_dict['choices'][0]['message'])
        print(res_dict['choices'][0]['message']['content'])
    else:
        print('Error')