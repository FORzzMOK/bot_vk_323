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
	while True:#бесконечный цикл
		for event in longpoll.listen():#если что то произошло в лонгпуле
			if event.from_chat and event.chat_id == 50 :#если это новое сообщение то выполнится следующее
				#response = event.text#переводит сообщение в нижний регистр и присваеват response
				#print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))#время отправки сообщения
				#print('Текст сообщения: ' + str(event.text))#Текст сообщения
				if "Hello Bot" in str(event.text):
					vk_session.method('messages.send', {'chat_id': 50, 'message': 'Hello World', 'random_id':0})#оправится сообщение
					time.sleep(1)
				if 'IP' in str(event.text):
					Ip = IP_CALCULATION(event)
					vk_session.method('messages.send', {'chat_id': 50, 'message': Ip, 'random_id':0})
					time.sleep(1)
def IP_CALCULATION(other):
	MessageList = other.text.split()
	return Skript.Start(MessageList)

if __name__ == "__main__":
	StartProgramm()