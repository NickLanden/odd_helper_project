from bs4 import BeautifulSoup
from datetime import timedelta
import requests_cache

from constants import MAIN_URL
from telegram import telegram_send_message


def get_news(session):
    response = session.get(MAIN_URL)

    soup = BeautifulSoup(response.text, features='lxml')

    div_tag = soup.find('div', attrs={'class': 'l-table'})
    top_news_table = div_tag.find(
        'div',
        attrs={'data-vr-zone': 'Топ новости'}
    )
    news_tags = top_news_table.find_all(
        'div',
        attrs={'class': 'main__feed js-main-reload-item'}
    )

    top5_news = []
    for i in range(5):
        news = news_tags[i]
        news_link = news.find('a')['href']
        news_title = news.find(
            'span',
            attrs={'class': 'main__feed__title'}
        ).text

        top5_news.append(
            (news_title, news_link)
        )

    return top5_news


def main():
    session = requests_cache.CachedSession(
        expire_after=timedelta(hours=1)
    )
    top5_news = get_news(session)
    telegram_send_message(top5_news)


if __name__ == '__main__':
    main()
