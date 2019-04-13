#!python3
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import time
import Skript
from datetime import datetime

vk_session = vk_api.VkApi(token = "a102c34010ab9a8b393041f37c97d30ceeb7531b748fbadfc4f6e210ce9f094b01d1c08bbdfc8d130e10b")

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def StartProgramm():
	while True:
		for event in longpoll.listen():
			if event.from_chat  and event.chat_id == 50 and event.type == VkEventType.MESSAGE_NEW and not(event.from_me):
				response = event.text.lower()
				if 'hello_bot' in event.text.lower():
					vk_session.method('messages.send', {'chat_id': 50, 'message': 'Hello World', 'random_id':0})
					time.sleep(1)
				elif 'IP' in event.text:
					vk_session.method('messages.send', {'chat_id': 50, 'message': Skript.Start(event.text.split()), 'random_id':0})
					time.sleep(1)
if __name__ == "__main__":
	StartProgramm()