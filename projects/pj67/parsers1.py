import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("article", class_="tm-articles-list__item")
        for item in news:
            title = item.find("a", class_="tm-title__link").find("span").text
            href = f"https://habr.com{item.find("a", class_="tm-title__link")['href']}"
            author = item.find("a", class_="tm-user-info__username").text
            self.res.append({
                "title": title,
                "href": href,
                "author": author,
            })

    def save(self):
        with open(self.path, "w", encoding="UTF-8") as f:
            i = 1
            for item in self.res:
                f.write(
                    f"Новость № {i}\n\nНазвание: {item['title']}\nАвтор: {item["author"]}\nСсылка: {item["href"]}"
                    f"\n\n{'*' * 30}\n")

                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
