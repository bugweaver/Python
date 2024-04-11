import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    c1 = (f'{soup.find_all("div", class_="my-city__item")[0].find_all("span")[0].text}:'
          f' {soup.find_all("div", class_="my-city__item")[0].find_all("span")[2].text}'
          f', {soup.find_all("div", class_="my-city__item")[0].find_all("span")[3].text}')

    c2 = (f'{soup.find_all("div", class_="my-city__item")[1].find_all("span")[0].text}:'
          f' {soup.find_all("div", class_="my-city__item")[1].find_all("span")[2].text}'
          f', {soup.find_all("div", class_="my-city__item")[1].find_all("span")[3].text}')

    c3 = (f'{soup.find_all("div", class_="my-city__item")[2].find_all("span")[0].text}:'
          f' {soup.find_all("div", class_="my-city__item")[2].find_all("span")[2].text}'
          f', {soup.find_all("div", class_="my-city__item")[2].find_all("span")[3].text}')

    c4 = (f'{soup.find_all("div", class_="my-city__item")[3].find_all("span")[0].text}:'
          f' {soup.find_all("div", class_="my-city__item")[3].find_all("span")[2].text}'
          f', {soup.find_all("div", class_="my-city__item")[3].find_all("span")[3].text}')

    return f'{c1}\n{c2}\n{c3}\n{c4}'


def main():
    url = "https://www.timeanddate.com/weather/"
    print(get_data((get_html(url))))


if __name__ == '__main__':
    main()
