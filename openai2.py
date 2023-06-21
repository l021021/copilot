import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message']['content'])
# print(response['choices'][0]['message']['content'])
# 解析response的数据结构