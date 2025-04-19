from openai import OpenAI # 导入OpenAI

client = OpenAI(base_url = "https://api.deepseek.com",
                api_key  = "")

completion = client.chat.completions.create(
  model="deepseek-chat", # this field is currently unused
  messages=[
    {"role": "user",
    "content": "你好"}
  ],
  temperature=0.7,
)
print(completion.choices[0].message.content)# 输出文案