import base64
import requests
import telebot
import spotipy
import database
from spotipy.oauth2 import SpotifyClientCredentials
import os

database.userInfo()

TOKEN = '6530213261:AAG2YNVijRIPp_0N_IuwgxfHqaVRjMtwZ3g'
client_id = '7cfaef72656e4024bf7b3b5cd88560e4'
client_secret = '1acef0b00d3340ccbee45d788bc3ea3d'

bot = telebot.TeleBot(TOKEN)
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

user_language = {}
sent_tracks_count = 0  # Добавляем переменную для отслеживания количества отправленных треков


def get_or_create_user(user: telebot.types.User) -> database.userInfo:
    '''
    Отримання інформації про користувача з бази даних або створення нового запису.

    Параметри:
    user (telebot.types.User): Користувач телеграму.

    Повертає:
    database.userInfo: Об'єкт, що містить інформацію про користувача.

    '''
    user_info, created = database.userInfo.get_or_create(
        user_id=user.id,
        defaults={'username': user.username}
    )
    return user_info


def get_access_token(client_id: str, client_secret: str) -> str:
    '''
    Отримання токену доступу для автентифікації на Spotify API.

    Параметри:
    client_id (str): Ідентифікатор клієнта Spotify.
    client_secret (str): Секретний ключ клієнта Spotify.

    Повертає:
    str: Токен доступу.

    '''
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode(),
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')


def search_tracks(query: str, access_token: str, limit: int = 5) -> list:
    '''
    Пошук треків на Spotify за запитом.

    Параметри:
    query (str): Запит для пошуку треків.
    access_token (str): Токен доступу для автентифікації на Spotify API.
    limit (int): Кількість треків, які потрібно повернути (за замовчуванням 5).

    Повертає:
    list: Список знайдених треків у форматі JSON.

    '''
    url = 'https://api.spotify.com/v1/search'
    params = {
        'q': query,
        'type': 'track',
        'limit': limit
    }
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data.get('tracks', {}).get('items', [])


@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):
    '''
    Обробник команди /start.

    Параметри:
    message (telebot.types.Message): Повідомлення від користувача.

    '''
    global sent_tracks_count  # Объявляем использование глобальной переменной
    sent_tracks_count = 0  # Обнуляем счетчик отправленных треков при каждом запуске бота
    user_info = get_or_create_user(message.from_user)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    markup.add(telebot.types.KeyboardButton("🇺🇸 English"), telebot.types.KeyboardButton("🇺🇦 Українська"))
    bot.send_message(message.chat.id, 'Оберіть вашу мову / Choose your language:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["🇺🇸 English", "🇺🇦 Українська"])
def handle_language(message):
    user_language[message.chat.id] = message.text
    if message.text == "🇺🇸 English":
        greeting_message = "Hello! Please type the name of the song you want to search for."
    elif message.text == "🇺🇦 Українська":
        greeting_message = "Привіт! Будь ласка, введіть назву пісні, яку ви хочете знайти."
    bot.send_message(message.chat.id, greeting_message)


@bot.message_handler(func=lambda message: message.text is not None)
def handle_message(message: telebot.types.Message):
    '''
    Обробник текстових повідомлень.

    Параметри:
    message (telebot.types.Message): Повідомлення від користувача.

    '''
    global sent_tracks_count  # Объявляем использование глобальной переменной

    if message.content_type == 'text':
        query = message.text
        language = user_language.get(message.chat.id, "🇺🇸 English")
        access_token = get_access_token(client_id, client_secret)
        tracks = search_tracks(query, access_token)
        if tracks:
            track = tracks[0]
            artists = ', '.join([artist.get('name') for artist in track.get('artists', [])])
            if language == "🇺🇸 English":
                response_message = (
                    f"Name: {track.get('name')}\n"
                    f"Artist: {artists}\n"
                    f"Album: {track.get('album', {}).get('name')}\n"
                    f"Link: {track.get('external_urls', {}).get('spotify')}"
                )
            elif language == "🇺🇦 Українська":
                response_message = (
                    f"Назва: {track.get('name')}\n"
                    f"Виконавець: {artists}\n"
                    f"Альбом: {track.get('album', {}).get('name')}\n"
                    f"Посилання: {track.get('external_urls', {}).get('spotify')}"
                )
            bot.send_message(message.chat.id, response_message)
            preview_url = track.get('preview_url')
            if preview_url:
                bot.send_message(message.chat.id, f"Preview of the song: {preview_url}")
            else:
                bot.send_message(message.chat.id, "Unfortunately, there is no preview available for this song.")

            sent_tracks_count += 1  # Увеличиваем счетчик отправленных треков

            # Проверяем, является ли количество отправленных треков кратным 5
            if sent_tracks_count % 5 == 0:
                if language == "🇺🇸 English":
                    support_message = "Thank you for using our bot!"
                elif language == "🇺🇦 Українська":
                    support_message = "Дякую що використали наш бот якщо ви маєте можливість пітримайте нас!"
                bot.send_message(message.chat.id, support_message)

        else:
            if language == "🇺🇸 English":
                bot.send_message(message.chat.id, 'Nothing found for your query.')
            elif language == "🇺🇦 Українська":
                bot.send_message(message.chat.id, 'За вашим запитом нічого не знайдено.')
    else:
        # Если сообщение не текстовое (например, это файл), отправляем сообщение о невозможности обработки
        language = user_language.get(message.chat.id, "🇺🇸 English")
        if language == "🇺🇸 English":
            bot.send_message(message.chat.id, "I'm sorry, I can't process media files.")
        elif language == "🇺🇦 Українська":
            bot.send_message(message.chat.id, "Вибачте, я не можу обробляти медіафайли.")


@bot.message_handler(content_types=['photo', 'video', 'audio', 'document', 'voice', 'sticker'])
def handle_media(message: telebot.types.Message):
    '''
    Обробник медіафайлів.

    Параметри:
    message (telebot.types.Message): Повідомлення від користувача.

    '''
    language = user_language.get(message.chat.id, "🇺🇸 English")
    if language == "🇺🇸 English":
        bot.send_message(message.chat.id, "I'm sorry, I can't process media files.")
    elif language == "🇺🇦 Українська":
        bot.send_message(message.chat.id, "Вибачте, я не можу обробляти медіафайли.")


# Периодически обнуляем счетчик отправленных треков
# Например, каждый час
import time

while True:
    bot.polling()
    time.sleep(3600)