import asyncio
from aiogram import Bot, Dispatcher, types
import datetime


# Channel = "k2023_bot_Channel"
# Token = 6767478787:AAFKEClm_JlnWJsWLeCrHHnwiDGVi39940g
# Channel ID = "1002122785379"


async def send_time():
    token = "6767478787:AAFKEClm_JlnWJsWLeCrHHnwiDGVi39940g"  # 내 채널 봇의 토큰 입력
    public_chat_name = '@k2023_bot_Channel'  # 내 채널의 username 입력

    bot = Bot(token=token)

    # 시간 보내는 함수
    async def job():
        # 현재 시간과 알림 회피 시간 설정
        now = datetime.datetime.now()
        if now.hour >= 23 or now.hour <= 6:
            return
        text = "현재 시간: " + now.strftime('%H:%M:%S')
        await bot.send_message(chat_id=public_chat_name, text=text)

    # 알림 보내는 시간 단위 설정 (초 단위)
    while True:
        await job()
        await asyncio.sleep(1800)


async def main():
    await send_time()


if __name__ == "__main__":
    repeat = asyncio.get_event_loop()
    repeat.run_until_complete(main())