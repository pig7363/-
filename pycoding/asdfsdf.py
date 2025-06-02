from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

messages = [{
    'role': 'system',
    'content': 'Please end the message with "Wow!"' #시스템 프롬프트
    }]
while True:
    msg = input('Write a message? ')
    messages.append({
        'role': 'user',
        'content': msg #유저 프롬프트
    })

    completion = client.chat.completions.create(
        model="meta-llama/llama-3.3-8b-instruct:free",
        messages=messages
    )
    messages.append(completion.choices[0].message)
    print(completion.choices[0].message.content)