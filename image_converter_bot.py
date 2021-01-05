import telebot
import os
import random
from PIL import Image

bot = telebot.TeleBot(' заперто ');

print('starting bot...')

@bot.message_handler(content_types=['document'])

def start(message):
	
	if not os.path.exists('tmp/{}'.format(message.chat.id)): #создаю папку для временных файлов 
		os.makedirs('tmp/{}'.format(message.chat.id))		 #с именем { user_id }

	global file_name
	
	if message.document.mime_type == 'image/jpeg': 
		keyboard = telebot.types.ReplyKeyboardMarkup(True) #кнопочки выбора формата
		keyboard.row('png', 'bmp', 'ico')				   #
		
		bot.send_message(message.chat.id,
		'{}, choose format for conversion'.format(message.document.mime_type),
		 reply_markup=keyboard)

		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		name_random = str(random.randint(1000, 1999)) #случайное циферное имя файла, чтобы небыло совпадений(на всякий)
		
		file_name = 'tmp/{0}/{1}'.format(message.chat.id, name_random)
		
		with open(file_name + '.jpg' ,'wb') as new_file: #сохраняю файл в папку '/tmp/{ user_id }'
			new_file.write(downloaded_file)
		
		bot.register_next_step_handler(message, convert_jpeg) #переход к следующей функции - хэндлеру

	elif message.document.mime_type == 'image/png':
		keyboard = telebot.types.ReplyKeyboardMarkup(True) #кнопочки выбора формата
		keyboard.row('jpg', 'bmp', 'ico')				   #

		bot.send_message(message.chat.id,
		'{}, choose format for conversion'.format(message.document.mime_type),
		 reply_markup=keyboard)

		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		name_random = str(random.randint(1000, 1999)) #случайное циферное имя файла, чтобы небыло совпадений(на всякий)

		file_name = 'tmp/{0}/{1}'.format(message.chat.id, name_random)
		
		with open(file_name + '.png' ,'wb') as new_file: #сохраняю файл в папку '/tmp/{ user_id }'
			new_file.write(downloaded_file)
		
		bot.register_next_step_handler(message, convert_png) #переход к следующей функции - хэндлеру

	elif message.document.mime_type == 'image/bmp':
		keyboard = telebot.types.ReplyKeyboardMarkup(True) #кнопочки выбора формата
		keyboard.row('jpg', 'png', 'ico')				   #

		bot.send_message(message.chat.id,
		'{}, choose format for conversion'.format(message.document.mime_type),
		 reply_markup=keyboard)

		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		name_random = str(random.randint(1000, 1999)) #случайное циферное имя файла, чтобы небыло совпадений(на всякий)

		file_name = 'tmp/{0}/{1}'.format(message.chat.id, name_random)
		
		with open(file_name + '.bmp' ,'wb') as new_file: #сохраняю файл в папку '/tmp/{ user_id }'
			new_file.write(downloaded_file)
		
		bot.register_next_step_handler(message, convert_bmp) #переход к следующей функции - хэндлеру

	elif message.document.mime_type == 'image/ico':
		keyboard = telebot.types.ReplyKeyboardMarkup(True) #кнопочки выбора формата
		keyboard.row('jpg', 'png', 'bmp')				   #

		bot.send_message(message.chat.id,
		'{}, choose format for conversion'.format(message.document.mime_type),
		 reply_markup=keyboard)

		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		name_random = str(random.randint(1000, 1999)) #случайное циферное имя файла, чтобы небыло совпадений(на всякий)

		file_name = 'tmp/{0}/{1}'.format(message.chat.id, name_random)
		
		with open(file_name + '.ico' ,'wb') as new_file: #сохраняю файл в папку '/tmp/{ user_id }'
			new_file.write(downloaded_file)
		
		bot.register_next_step_handler(message, convert_ico) #переход к следующей функции - хэндлеру
	
#	elif message.document.mime_type == 'image/svg+xml':
#		print('работает svg')
	
#	elif message.document.mime_type == 'image/gif':
#		print('работает gif')

def convert_ico(message):

	keyboard = telebot.types.ReplyKeyboardRemove(selective=False) # убираем кнопочки после нажатия

	if message.text == 'jpg':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_jpg = file_name + '.jpg'
		Image.open(file_name + '.ico').save(file_name_jpg) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_jpg, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'png':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_png = file_name + '.png'
		Image.open(file_name + '.ico').save(file_name_png) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_png, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'bmp':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_bmp = file_name + '.bmp'
		Image.open(file_name + '.ico').save(file_name_bmp) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_bmp, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	os.system('rm -r tmp/{}'.format(message.chat.id)) # удаляю временные файлы

def convert_bmp(message):

	keyboard = telebot.types.ReplyKeyboardRemove(selective=False) # убираем кнопочки после нажатия

	if message.text == 'jpg':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_jpg = file_name + '.jpg'
		Image.open(file_name + '.bmp').save(file_name_jpg) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_jpg, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'png':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_png = file_name + '.png'
		Image.open(file_name + '.bmp').save(file_name_png) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_png, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'ico':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_ico = file_name + '.ico'
		Image.open(file_name + '.bmp').save(file_name_ico) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_ico, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	os.system('rm -r tmp/{}'.format(message.chat.id)) # удаляю временные файлы

def convert_png(message):

	keyboard = telebot.types.ReplyKeyboardRemove(selective=False) # убираем кнопочки после нажатия

	if message.text == 'jpg':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_jpg = file_name + '.jpg'
		Image.open(file_name + '.png').save(file_name_jpg) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_jpg, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'bmp':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_bmp = file_name + '.bmp'
		Image.open(file_name + '.png').save(file_name_bmp) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_bmp, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'ico':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_ico = file_name + '.ico'
		Image.open(file_name + '.png').save(file_name_ico) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_ico, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	os.system('rm -r tmp/{}'.format(message.chat.id)) # удаляю временные файлы

def convert_jpeg(message):

	keyboard = telebot.types.ReplyKeyboardRemove(selective=False) # убираем кнопочки после нажатия
	
	if message.text == 'png':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_png = file_name + '.png'
		Image.open(file_name + '.jpg').save(file_name_png) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_png, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'bmp':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_bmp = file_name + '.bmp'
		Image.open(file_name + '.jpg').save(file_name_bmp) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_bmp, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	elif message.text == 'ico':

		bot.send_message(message.chat.id, 'converting...', reply_markup=keyboard)
		file_name_ico = file_name + '.ico'
		Image.open(file_name + '.jpg').save(file_name_ico) # конвертирую картинку при помощи PIL Image
		file_to_send = open(file_name_ico, "rb")
		bot.send_document(message.chat.id, file_to_send) # отправляю конвертированную картинку обратно

	os.system('rm -r tmp/{}'.format(message.chat.id)) # удаляю временные файлы

if __name__ == '__main__':
	bot.infinity_polling()

bot.polling(none_stop=True, interval=0)
