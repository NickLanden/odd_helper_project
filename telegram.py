from datetime import date
import os
import requests

from dotenv import load_dotenv

load_dotenv()


def telegram_send_message(object):
    token = os.environ.get("TELEGRAM_TOKEN")
    telegram_url = f'https://api.telegram.org/bot{token}/sendMessage'

    text_message = f'ТОП-5 НОВОСТЕЙ на {date.today()}\n'
    news_number = 1

    for news in object:
        title = news[0]
        link = news[1]
        text_message += f'{news_number}.  <a href="{link}">{title}</a>\n'
        news_number += 1

    response = requests.post(
        telegram_url,
        data={'chat_id': '418681641',
              'parse_mode': 'HTML',
              'disable_notification': True,
              'disable_web_page_preview': True,
              'text': text_message}
    )
    print(response)

if __name__ == '__main__':
    telegram_send_message()