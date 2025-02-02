import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup

from tech_news.database import create_news


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
    selector = Selector(html_content)
    soup = BeautifulSoup(html_content, "html.parser")

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css("span.fn a::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    summary = soup.find("div", {"class": "entry-content"}).p.text
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer.strip(),
        "reading_time": int(reading_time.split()[0]),
        "summary": summary.strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    url_news = []
    info_news = []

    while len(url_news) < amount:
        html_contetnt = fetch(url)
        url_news.extend(scrape_updates(html_contetnt))
        url = scrape_next_page_link(html_contetnt)

        if not url:
            break

    first_news = url_news[:amount]

    for news in first_news:
        html_contetnt = fetch(news)
        dict_news = scrape_news(html_contetnt)
        info_news.append(dict_news)

    create_news(info_news)

    return info_news
