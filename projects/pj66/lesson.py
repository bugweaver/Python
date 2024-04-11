# import csv
#
# with open("data.csv", encoding="UTF-8") as f:
#     fild_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, fieldnames=fild_names)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f'{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']}')
#         count += 1
# import csv
#
# with open('student.csv', 'w', encoding="UTF-8") as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', "Класс", "Возраст"])
#     writer.writerow(['Женя', 9, 15])
#     writer.writerow(['Саша', 5, 12])
#     writer.writerow(['Маша', 11, 18])


# import csv
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w', encoding="UTF-8") as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
# with open('data_new.csv',encoding="UTF-8") as f:
#     print(f.read())

# import csv
#
# with open('stud.csv', 'w', encoding='UTF-8') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})

# import csv
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('stud.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# import requests
# import json
# import csv

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# with open('stud2.csv', 'w', encoding='UTF-8') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)

# Парсинг

# C


# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all("div", {'data-set': "salary"})
# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, 'html.parser')

# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    p1 = soup.find('header', id="masthead").find("p", class_="site-title").text
    return p1


def main():
    url = "https://ru.wordpress.org/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
