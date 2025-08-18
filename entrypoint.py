import sys
import telegram
import asyncio
from md2tgmd import escape
import json
import os

BOT_TOKEN = sys.argv[1]
CHAT_ID = sys.argv[2]
message = sys.argv[3]

bot = telegram.Bot(token=BOT_TOKEN)

async def main():
    # 发送消息并捕获返回值
    result = await bot.send_message(chat_id=CHAT_ID, text=escape(message), parse_mode="MarkdownV2")
    
    # 转成 JSON 字符串
    result_json = json.dumps(result.to_dict())
    
    # 写入 GitHub Actions output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"response={result_json}\n")

asyncio.run(main())
