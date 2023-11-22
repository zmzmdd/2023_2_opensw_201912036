from aiogram import Bot, Dispatcher
from openai import OpenAI
import telegram
import asyncio

token = "6767478787:AAFKEClm_JlnWJsWLeCrHHnwiDGVi39940g"  # 내 채널 봇의 토큰 입력
public_chat_name = '@k2023_bot_Channel'  # 내 채널의 username 입력

bot = telegram.Bot(token=token)

client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "what is your question?"},
        {"role": "user", "content": "please explain about earthquake"}
    ]
)
text = completion.choices[0].message.content
asyncio.run(bot.sendMessage(chat_id=public_chat_name, text=text))
