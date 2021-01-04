import telebot
from bs4 import BeautifulSoup
import requests as req

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Ну здарова, ты кароче меня призвал кнопкой /start, если нужна помощь, то отправь "/help"')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Сейчас я могу ответить тебе на слова привет и пока, отвечать на картинки'
                                      'а так же копировать остальные твои сообщения, но мой хозяин сказал,что скоро я'
                                      ' стану умнее. Надеюсь на это...')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет дарагой <3')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'покакаешь дома((')
    else:
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['photo'])
def send_text(message):
    bot.send_message(message.chat.id, 'ляпота!')


@bot.message_handler(commands=['statistic'])
def statistic(m):
    resp = req.get("https://ranobelib.me/bezdna")
    soup = BeautifulSoup(resp.text, 'lxml')
    num_of_readers = ''

    for i in soup.text.split('\n'):
        if 'В закладках у людей ' in i:
            num_of_readers = i

    tags = soup.find_all(['div', 'p'])
    views = ''

    for tag in tags:
        for j in tag.text.split():
            if 'просм' in j.lower():
                views = j
    bot.send_message(m.chat.id, num_of_readers)
    bot.send_message(m.chat.id, views)


bot.polling()
