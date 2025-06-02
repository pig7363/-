# 1번 문제
import requests
import json

api_key = ""
model_name = "meta-llama/llama-3.3-8b-instruct:free"

system_prompt = {
    "role": "system",
    "content": "사용자가 입력한 텍스트를 분석하여, 여섯 가지 기본 감정(기쁨, 슬픔, 분노, 놀람, 혐오, 두려움)에 해당하는 감정 점수를 0에서 1사이의 값으로 출력하세요."
}

user_input = input("감정을 분석할 문장을 입력하세요: ")

messages = [
    system_prompt,
    {
        "role": "user",
        "content": user_input
    }
]

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>"
    },
    data=json.dumps({
        "model": model_name,
        "messages": messages
    })
)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print("Error")

# 2번 문제
import requests
import json

api_key = ""
model_name = "meta-llama/llama-3.3-8b-instruct:free"

system_prompt = {
    "role": "system",
    "content": "Recommend one dinner dish that can be made with the ingredients provided by the user, and explain the recipe."
}

ingredient_input = input("가지고 있는 재료를 입력하세요: ")

messages = [
    system_prompt,
    {
        "role": "user",
        "content": ingredient_input
    }
]

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>"
    },
    data=json.dumps({
        "model": model_name,
        "messages": messages
    })
)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code)

# 3-1번문제
import requests
import json

api_key = ""
model_name = "meta-llama/llama-4-scout:free"

image_url = input("이미지 URL을 입력하세요: ")

system_prompt = {
    "role": "system",
    "content": "너는 사용자의 이미지와 말투를 분석해서 조언을 해주는 어시스턴트야."
}

user_prompt = {
    "role": "user",
    "content": f"다음 이미지를 보고 날씨를 예측해줘: {image_url}"
}

messages = [system_prompt, user_prompt]

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>"
    },
    data=json.dumps({
        "model": model_name,
        "messages": messages
    })
)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code)

# 3-2번 문제
import requests
import json

api_key = ""
model_name = "meta-llama/llama-4-scout:free"

plan = input("오늘의 계획을 입력하세요: ")

weather_info = "사진 속 하늘은 구름이 조금 낄 정도로 맑고 청명한 하늘인 것 같습니다. 바다 또한 잔잔한 상태를 유지하고 있네요. 이 사진을 통해 추측해 보면, 현재 날씨는 화창하고 쾌청한 날씨로 추정됩니다."

system_prompt = {
    "role": "system",
    "content": "너는 사용자의 이미지와 말투를 분석해서 조언을 해주는 어시스턴트야."
}

user_prompt = {
    "role": "user",
    "content": f"오늘 계획은 {plan} 이고 밖의 날씨는 {weather_info} 한 데, 옷을 어떻게 입는게 좋을까?"
}

messages = [system_prompt, user_prompt]

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>"
    },
    data=json.dumps({
        "model": model_name,
        "messages": messages
    })
)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code)