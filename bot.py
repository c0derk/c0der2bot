
# -*- coding: utf-8 -*-

import telebot
import random
import time
import datetime
import json
import urllib2

flipper = ['Орел','Решка']
phares1 = ['Як Сергій та Лінукс', 'Як Михайло та Мафіозник', 'Як Валерія та її телефон', 'Як Час та Герб']
phares2 = ['Як Сергійко та Іван', 'Як Марина та умер мужик', 'Як Геї та Дота']
phares3 = ['Як Україна та Європа', 'Як Влад та Глад Валакас', 'Як Артем та круасан']
max_temp = ['макс. ']
min_temp = ['мін. ']
emojiphr3 = [' ❤️', ' 💋', ' 💕', ' 💓']
emojiphr2 = [' 💘', ' 💝', ' 💖', ' ♥️']
emojiphr1 = [' 😻', ' 😍',' 🥰', ' 😘']

cute1 = '''	 ᠌ ᠌ ᠌᠌ ᠌ ᠌ ᠌ ᠌ ᠌○ ＿＿＿＿＿
    								‖    	 							 	|
    								‖    100!			|
    								‖    	 							 	|
    								‖￣￣￣￣
  ∧＿∧‖
 (`･ω･‖
 丶 つ０
  しーＪ'''

jokes = ['''Дружина входить у ванну і бачить: на вагах стоїть чоловік і втягує живіт.
- Думаєш, це допоможе?
- Звичайно! Як я інакше побачу цифри?!''',
'''Кажуть, ваш чоловік в лікарні. Що з ним?
- Справа в тому, що він злазив з даху по драбині, яку я прибрала.''',
'''Вовочка підходить до Марійки й каже:
— Марусю, можна використати тебе як жінку?
— Які в тебе думки вульгарні!
— Це, Марусю, в тебе вульгарні, а в мене м’ячик у жіночий туалет закотився!''',
'''— Андрійко, ти навіщо стукнув дядька Петра цеглиною по голові?
— Я більше не буду…
— А йому більше й не треба…''',
'''Звичайнісіньке українське село.Ніч.У кімнаті на печі сплять діти.Батьки вирішили зайнятися коханням.У самий розпал процесу з печі лунає голос дитини:
-І я хочу вареників.
-Та яких тобі вареників посеред ночі,синку.
-А чим це ви там так смачно чавкаєте?''',
'''Матінка говорить Сергійку:
- Мені пташка нашептала, що ти, синку, наркотиками балуєшся.
- Це ти, матінко, балуєшся, якщо тобі пташки шепочуть.''',
'''Дівчинка виходить із ванної і говорить Артемові:
- В тебе в ванній висять два рушники: один під буквою «М», другий під буквою «Ж».
Я взяла те, що під буквою «Ж».
Я правильно розуміла, «Ж» – для жінок, «М» – для мужчин.
- Ні, «М» – для морди…''',
'''- А я Наташці кільце подарував. Нехай тепер пострибає від радості.
- Золоте?
- Ні-і, баскетбольне.''',
'''Дві блондинки в гуртожитку. Одна пролила кип'яток на підлогу та й каже:
- Як цю воду витерти, вона ж гаряча.
Друга каже:
- А ти долий холодної і витирай.''',
'''Один хлопчик не вмів вимовляти слово шість, прийшов якось одного разу у магазин і каже продавцеві:
- Дайте мені сім пачок масла, одну не треба.''',
'''- У тебе зараз щось в житті відбувається?
- Так.
- Що?
- У мене макарони варяться.
- А якщо серйозно?
- Ти думаєш є сенс брехати щодо макаронів?''',
'''- Вчора у нашу квартиру заліз злодій.
- І що? Взяв щось?
- Та де там! Лежить у лікарні. Дружина подумала, що це я повернувся так пізно...''',
'''Чоловік вночі говорить дружині:
- Дорога, а давай в рольові ігри пограємо?
- Як це?
- Ну, ти ніби Червона Шапочка, а я досвідчений вовк!
- Давай!
- Ну, тоді йди, пиріжки пекти!''',
'''Дружина:
- Я у тебе як Попелюшка - стіраю, прибираю, готую...
Чоловік у відповідь:
- Я ж тобі казав, вийдеш за мене - жити будеш як в казці!''',
'''- Вона мені зрадила цієї ночі.
- А ти що?
- Я помстився їй тиждень тому.''',
'''Якось поставив собі Сергій Лінукс...''']
confirm_responce = ['Так', 'Ні', 'зсенсом', 'Можливо', 'Я не знаю']
joke_responce = ['Посмійтеся будь ласочка ☺️', 'Ви ж посмієтеся? ☺️', 'Це був файний жарт, чи не так? ☺️', 'Я чекаю на вашу усмішку ☺️']

reshka_flip = 'CAADAgADGwADsdLfFj4BfFUxRg-pAg'
orel_flip = 'CAADAgADHAADsdLfFr5ITr98k0M7Ag'


salo_sti = ['CAADAgADHQADsdLfFteT7ZeW27UWAg', 'CAADAgADHgADsdLfFvxy3T92Dbf6Ag', 'CAADAgADHwADsdLfFoHja4JE2si3Ag', 'CAADAgADIAADsdLfFqD1h1aoRv2wAg', 'CAADAgADIQADsdLfFuYCL6s51bs2Ag', 'CAADAgADIgADsdLfFiJAMh1L3o1fAg', 'CAADAgADIwADsdLfFkoPGtJvKlBtAg', 'CAADAgADJAADsdLfFgr-SD2ABN3yAg', 'CAADAgADJQADsdLfFt2q5uc-WR3gAg', 'CAADAgADJgADsdLfFme72ncofDDAAg', 'CAADAgADJwADsdLfFgEBHmNmAqqSAg']



Token = '736629516:AAGDuxxoaK1LEloeVSixQjCazN2GP6F1qy4'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['test'])
def testmsg(message):
	bot.send_message(message.chat.id, message.date)

@bot.message_handler(content_types=["new_chat_members"])
def new_chat(message):
	bot.reply_to(message, 'Привіт, шановний друже!')

@bot.message_handler(content_types=["left_chat_member"])
def left_chat(message):
	bot.reply_to(message, 'Помер Дядько')

@bot.message_handler(content_types=['sticker'])
def agressive_to_sticker(message):
	if random.randint(1,100) <= 25:
		bot.send_message(message.chat.id, 'Йдіть в дупу зі своїми стікерами 😡')

@bot.message_handler(commands=['salo'])
def upload_salo_sticker(message):
	time.sleep(.1)
	bot.send_sticker(message.chat.id, random.choice(salo_sti))

@bot.message_handler(commands=['joke'])
def get_jokes_msg(message):
	bot.send_message(message.chat.id, random.choice(jokes))
	time.sleep(.5)
	bot.send_message(message.chat.id, random.choice(joke_responce))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Доброго дня, Пані та Панове")
	
@bot.message_handler(commands=['roll'])
def get_random(message):
	if random.randint(1, 100) == 100:
		bot.send_message(message.chat.id, cute1)
	else:
		bot.send_message(message.chat.id, 'Вам випадає число '+str(random.randint(1, 99)))

@bot.message_handler(commands=['flip'])
def get_flip(message):
	time.sleep(.41)
	if random.choice(flipper) == 'Орел':
		bot.send_message(message.chat.id, 'Вам випадає Орел')
		bot.send_sticker(message.chat.id, orel_flip)
	elif random.choice(flipper) == 'Решка':
		bot.send_message(message.chat.id, 'Вам випадає Решка')
		bot.send_sticker(message.chat.id, reshka_flip)
	else:
		pass
	
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, text='Я вмію шипперити та роблю це українською 😊')

@bot.message_handler(commands=['shipp'])
def Shipper(message):
	if message.chat.id == -1001205081662 or message.chat.id == -1001343961111 or message.chat.id == 383767217:	
		cooldown = 60*60*12
		test_cooldown = 60
		time_now = time.time()
		handle = open('time.txt','r')
		data = handle.read()
		handle.close()	
		if time_now-float(data) >= cooldown:
			bot.send_message(message.chat.id, random.choice(phares1)+random.choice(emojiphr1))
			time.sleep(.3)
			bot.send_message(message.chat.id, random.choice(phares2)+random.choice(emojiphr2))
			time.sleep(.3)
			bot.send_message(message.chat.id, random.choice(phares3)+random.choice(emojiphr3))
			id_key = ['383767217Sergey', '532257360Lera', '649450266Katyusha', '550191195Katya', '645098509Ivan', '623019598Artem', '586905500Nikita', '563715109Misha', '557697647Julia', '505150515Nastya', '460966001Vlad', '445197138Serhiyko', '712378317Tanya', '693321194Marina', '408109305Danil']
			#markdown = '''[+++++++++](tg://user?id='''+id_key+''')'''
			list_of_randoms = random.sample(id_key, 2)
			first_random_item = list_of_randoms[0]
			second_random_item = list_of_randoms[1]
			markdown1 = '''['''+(first_random_item[9:30])+'''](tg://user?id='''+str(first_random_item[0:9])+''')'''
			markdown2 = '''['''+(second_random_item[9:30])+'''](tg://user?id='''+str(second_random_item[0:9])+''')'''
			bot.send_chat_action(message.chat.id, 'typing')
			time.sleep(3)
			bot.send_message(message.chat.id, 'Застигають у вічному коханні '+(markdown1)+' + '+(markdown2)+' = '+random.choice(emojiphr2), parse_mode='Markdown' )
			rewrite = open('time.txt', 'w')
			new_time = str(time.time())
			rewrite.write(new_time)
			rewrite.close()
		else:
			remain_time = str(int((cooldown-(time_now-float(data)))/60/60))
			bot.send_message(message.chat.id, 'Мені потрібен час на перезарядку ~ '+remain_time+'год.')

	else:
		bot.send_message(message.chat.id, 'Ця функція є ексклюзивною для групи Херсон Паті')

@bot.message_handler(commands=['weather'])
def getWeather24(message):
	weather_url = 'http://api.openweathermap.org/data/2.5/forecast?q=Kherson,ua&lang=ua&units=metric&cnt=8&appid=70733a38882077ca17d167f9ee4acede'
	url_weather = urllib2.urlopen(weather_url)
	data = json.loads(url_weather.read())
	for i in data['list'][0:1]:
		first = (i['dt_txt'][11:16])
		first_date = (i['dt_txt'][8:10])
		first_date_plus = (i['dt_txt'][5:7])
		first_temp_current = i['main']['temp']
		first_temp_min = i['main']['temp_min']
		first_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos1 = (u['description'].capitalize())
	for i in data['list'][1:2]:
		second = (i['dt_txt'][11:16])
		second_date = (i['dt_txt'][8:10])
		second_date_plus = (i['dt_txt'][5:7])
		second_temp_current =i['main']['temp']
		second_temp_min = i['main']['temp_min']
		second_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos2 = (u['description'].capitalize())
	for i in data['list'][2:3]:
		third = (i['dt_txt'][11:16])
		third_date = (i['dt_txt'][8:10])
		third_date_plus = (i['dt_txt'][5:7])
		third_temp_current =i['main']['temp']
		third_temp_min = i['main']['temp_min']
		third_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos3 = (u['description'].capitalize())
	for i in data['list'][3:4]:
		fourth = (i['dt_txt'][11:16])
		fourth_date = (i['dt_txt'][8:10])
		fourth_date_plus = (i['dt_txt'][5:7])
		fourth_temp_current =i['main']['temp']
		fourth_temp_min = i['main']['temp_min']
		fourth_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos4 = (u['description'].capitalize())
	for i in data['list'][4:5]:
		fifth = (i['dt_txt'][11:16])
		fifth_date = (i['dt_txt'][8:10])
		fifth_date_plus = (i['dt_txt'][5:7])
		fifth_temp_current =i['main']['temp']
		fifth_temp_min = i['main']['temp_min']
		fifth_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos5 = (u['description'].capitalize())
	for i in data['list'][5:6]:
		sixth = (i['dt_txt'][11:16])
		sixth_date = (i['dt_txt'][8:10])
		sixth_date_plus = (i['dt_txt'][5:7])
		sixth_temp_current =i['main']['temp']
		sixth_temp_min = i['main']['temp_min']
		sixth_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos6 = (u['description'].capitalize())
	for i in data['list'][6:7]:
		seventh = (i['dt_txt'][11:16])
		seventh_date = (i['dt_txt'][8:10])
		seventh_date_plus = (i['dt_txt'][5:7])
		seventh_temp_current =i['main']['temp']
		seventh_temp_min = i['main']['temp_min']
		seventh_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos7 = (u['description'].capitalize())
	for i in data['list'][7:8]:
		eightth = (i['dt_txt'][11:16])
		eightth_date = (i['dt_txt'][8:10])
		eightth_date_plus = (i['dt_txt'][5:7])
		eightth_temp_current =i['main']['temp']
		eightth_temp_min = i['main']['temp_min']
		eightth_temp_max = i['main']['temp_max']
		for u in i['weather']:
			pizdos8 = (u['description'].capitalize())
	responce = '🔸 '.decode('utf-8') + first_date + '-' + first_date_plus+' ('.decode('utf-8')+ first +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(first_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(first_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos1+')\n' + '🔸 '.decode('utf-8') + second_date+'-'+second_date_plus +' ('.decode('utf-8')+ second +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(second_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(second_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos2+')\n' +'🔸 '.decode('utf-8') + third_date+'-'+third_date_plus +' ('.decode('utf-8')+ third +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(third_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(third_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos3+')\n' + '🔸 '.decode('utf-8') + fourth_date+'-'+fourth_date_plus +' ('.decode('utf-8')+ fourth +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(fourth_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(fourth_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos4+')\n'+ '🔸 '.decode('utf-8') + fifth_date+'-'+fifth_date_plus +' ('.decode('utf-8')+ fifth +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(fifth_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(fifth_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos5+')\n'+ '🔸 '.decode('utf-8') + sixth_date+'-'+sixth_date_plus +' ('.decode('utf-8')+ sixth +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(sixth_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(sixth_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos6+')\n'+ '🔸 '.decode('utf-8') + seventh_date+'-'+seventh_date_plus +' ('.decode('utf-8')+ seventh +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(seventh_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(seventh_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos7+')\n'+ '🔸 '.decode('utf-8') + eightth_date+'-'+ eightth_date_plus +' ('.decode('utf-8')+ eightth +') : '+'\n ''🌡 ‖'.decode('utf-8')+random.choice(min_temp).decode('utf-8') +str(round(eightth_temp_min, 1)) +'℃‖'.decode('utf-8')+random.choice(max_temp).decode('utf-8') +str(round(eightth_temp_max, 1)) +'℃‖ '.decode('utf-8')+ '⛅ ('.decode('utf-8')+pizdos8+')\n'
	bot.send_message(message.chat.id, responce)
	
@bot.message_handler(commands=['currency'])
def get_currency(message):
	currencyurl = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
	cur_json_obj = urllib2.urlopen(currencyurl).read()
	USD_to_UAH = json.loads(cur_json_obj)[0:1]
	for a in USD_to_UAH:
		#uahusd = '💵'.decode('utf-8') + ' До '.decode('utf-8') + a['base_ccy'] +' '+ a['buy'][0:5] +'-'+ 'Купівля'.decode('utf-8') +' ‖ '.decode('utf-8')+ a['sale'][0:5] +'-'+ 'Продаж'.decode('utf-8')
		uahusd = '$'.decode('utf-8') + ' До '.decode('utf-8') + a['base_ccy'] +' '+ a['buy'][0:5] +'-'+ 'Купівля'.decode('utf-8') +' ‖ '.decode('utf-8')+ a['sale'][0:5] +'-'+ 'Продаж'.decode('utf-8')
	EUR_to_UAH = json.loads(cur_json_obj)[1:2]
	for i in EUR_to_UAH:
		#uaheur = '💶'.decode('utf-8') + ' До '.decode('utf-8') + i['base_ccy'] +' '+ i['buy'][0:5] +'-'+ 'Купівля'.decode('utf-8') +' ‖ '.decode('utf-8')+ i['sale'][0:5] +'-'+ 'Продаж'.decode('utf-8')
		uaheur = '€'.decode('utf-8') + ' До '.decode('utf-8') + i['base_ccy'] +' '+ i['buy'][0:5] +'-'+ 'Купівля'.decode('utf-8') +' ‖ '.decode('utf-8')+ i['sale'][0:5] +'-'+ 'Продаж'.decode('utf-8')
	RUB_to_UAH = json.loads(cur_json_obj)[2:3]
	for s in RUB_to_UAH:
		uahrub = '₽'.decode('utf-8') + ' До '.decode('utf-8') + s['base_ccy'] +' '+ s['buy'][0:5] +'-'+ 'Купівля'.decode('utf-8') +' ‖ '.decode('utf-8')+ s['sale'][0:5] +'-'+ 'Продаж'.decode('utf-8')
	responce = uahusd +'\n' + uaheur+'\n' + uahrub
	bot.send_message(message.chat.id, responce)

#@bot.message_handler(commands=['cute'])
#def get_cute(message):
	#bot.send_message(message.chat.id, cute1)

@bot.message_handler(func=lambda message: True)
def Hello(message):
	if message.text == 'да?'.decode('utf-8') or message.text == 'Да?'.decode('utf-8') or message.text == 'сос мыслом'.decode('utf-8') or message.text == 'ДА?'.decode('utf-8'):
		if random.randint(1,100) <= 8:
			bot.send_message(message.chat.id, 'Хуй на')
		else:
			bot.send_message(message.chat.id, random.choice(confirm_responce))
	else:
		pass
	if message.text == 'Бот, привет'.decode('utf-8') or message.text == 'Бот,привет'.decode('utf-8') or message.text == 'бот,привет'.decode('utf-8') or message.text == 'бот, привет'.decode('utf-8') or message.text == 'Бот привет'.decode('utf-8') or message.text == 'бот привет'.decode('utf-8'):
		
		if time.localtime().tm_hour in range(6, 11):
			bot.send_message(message.chat.id, 'Доброго ранку')
		if time.localtime().tm_hour in range(12, 16):
			bot.send_message(message.chat.id, 'Доброго дня')
		if time.localtime().tm_hour in range(17, 23):
			bot.send_message(message.chat.id, 'Доброго вечора')
		if time.localtime().tm_hour in range(0,5):
			bot.send_message(message.chat.id, 'Чого ти не спиш?')
			
bot.infinity_polling()