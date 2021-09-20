import config
import telebot
from telebot import types
from datetime import date
bot = telebot.TeleBot(config.token)

# ~ @bot.message_handler(content_types=["text"])
# ~ def repeat_all_messages(message): # Название функции не играет никакой роли
    # ~ bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f'⚽⚽Бамжур, {message.from_user.first_name}!⚽⚽')


@bot.message_handler(content_types=["text"])
def start_score(message):
	score_answ = ['/score', 'score', 'счет', 'да']	
	if message.text.lower() == 'нет':
		bot.send_message(message.from_user.id, '😔')
	elif message.text.lower() == 'мяч':
		bot.send_message(message.from_user.id, '⚽')
	elif message.text.lower() == 'рожа':
		bot.send_message(message.from_user.id, '🥴')
		
	
	elif message.text.lower() in score_answ:
	# ~ if message.text == 'score':
		bot.send_message(message.from_user.id, "Кто играл в первой комманде?");
		bot.register_next_step_handler(message, first_team)
		# ~ else:
		# ~ bot.send_message(message.from_user.id, "Напиши '/start','/help' или '/score'");
	else:
		bot.send_message(message.from_user.id, '"/score" - записать счет игры\n "Рожа" - показать упоротую рожу')
def first_team(message):
	team1 = message.text
	bot.send_message(message.from_user.id, 'Кто играл во второй комманде?');
	bot.register_next_step_handler(message, second_team);
	with open('/home/freshharakl/mybot/score', 'a')as f:
		f.write(f'{date.today()}: {team1} vs ')

def second_team(message):
	team2 = message.text
	bot.send_message(message.from_user.id, 'Какой счет? "Первая комманда:Вторая комманда"');
	bot.register_next_step_handler(message, score);
	with open('/home/freshharakl/mybot/score', 'a')as f:
		f.write(team2 + ' : ')

def score(message):
	final_score = message.text
	bot.send_message(message.from_user.id, text='Ещё что-нибудь?')
	with open('/home/freshharakl/mybot/score', 'a') as f:
		f.write(final_score +'\n')

if __name__ == '__main__':
    bot.infinity_polling()
	
