from openai import OpenAI # 导入OpenAI

client = OpenAI(base_url = "https://api.deepseek.com",
                api_key  = "sk-e1efccd85ae142e980b6e31bb27a1f6e")

completion = client.chat.completions.create(
  model="deepseek-chat", # this field is currently unused
  messages=[
    {"role": "user",
    "content": "你好"}
  ],
  temperature=0.7,
)
print(completion.choices[0].message.content)# 输出文案