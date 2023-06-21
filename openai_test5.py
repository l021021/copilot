import openai

# 设置您的OpenAI API密钥
openai.api_key = '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'
# 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
# 调用GPT-3.5模型生成文本

# call the openai ChatCompletion endpoint
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)
# extract the response
print(response['choices'][0]['message']['content'])
