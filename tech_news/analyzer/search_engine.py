from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []
    for notice in news:
        test = (notice["title"], notice["url"])
        news_list.append(test)
    return news_list


# Requisito 8
def search_by_date(date):
    try:
        date_param = datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        raise ValueError("Data inválida")

    date_formated = date_param.strftime("%d/%m/%Y")
    news = search_news({"timestamp": date_formated})

    news_list = []
    for notice in news:
        test = (notice["title"], notice["url"])
        news_list.append(test)
    return news_list


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    news_list = []
    for notice in news:
        test = (notice["title"], notice["url"])
        news_list.append(test)
    return news_list
