import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None
    except requests.exceptions.HTTPError:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    url_news = selector.css(".entry-title > a::attr(href)").getall()
    if url_news:
        return url_news
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
