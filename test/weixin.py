# 导入模块
from wxpy import *
import json
import requests

def weixin():
    pass


# if __name__ == '__main__':
bot = Bot(console_qr=True, cache_path=True)
    # 机器人账号自身

print('九日AI已经启动')

def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "7c8cdb56b0dc4450a8deef30a496bd4c"
    payload = {
        "key": "f4aeb04521c34bb4aa1174b100cf3a1b",
        "info": text,
        "userid": "666"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return "[九日AI]  " + result["text"] + result["url"]
    else:
        return result["text"]


@bot.register(Group, TEXT)
def group_message(msg):
    if msg.is_at:
        print('[接收]' + str(msg))
        if (msg.type != 'Text'):
            ret = '[奸笑][奸笑]'
        else:
            ret = auto_ai(msg.text)
        print('[发送]' + str(ret))
        return ret


@bot.register(chats=[Friend])
def forward_message(msg):
    print('[接收]' + str(msg))

    if (msg.type != 'Text'):
        ret = '[奸笑][奸笑]'
    else:
        ret = auto_ai(msg.text)
    print('[发送]' + str(ret))
    return ret



embed()