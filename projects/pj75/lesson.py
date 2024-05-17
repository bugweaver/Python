# from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{a}} лет. Меня зовут {{n}}")
# msg = tm.render(n=name, a=age)
#
# print(msg)

# per = {'name': 'Игорь', 'age': 28}
#
# tm = Template("Мне {{p['age']}} лет. Меня зовут {{p.name}}")
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{p['age']}} лет. Меня зовут {{p.get_name()}}")
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Сочи'},
#     {'id': 4, 'city': 'Минск'},
#     {'id': 5, 'city': 'Ярославль'}
# ]

# link = """<select>
# {% for c in cities -%}
#     {%- if c.id > 3 -%}
#     <option value="{{ c['id']}}">{{ c['city']}}</option>
#     {% elif  c.city == "Москва" %}
#     <option >{{ c['city']}}</option>
#     {% else -%}
#     {{ c['city']  }}
#     {% endif -%}
# {% endfor -%}
# </select>"""
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# menu = [
#     {'url': 'index', 'title': 'Главная'},
#     {'url': 'news', 'title': 'Новости'},
#     {'url': 'about', 'title': 'О компании'},
#     {'url': 'shop', 'title': 'Магазин'},
#     {'url': 'contacts', 'title': 'Контакты'}
# ]
#
# link = """<ul>
#     {% for item in path %}
#         {% if item.url == 'index' %}
#         <li><a href="/{{ item.url }}" class='active'>{{ item.title }}</a></li>
#         {% else %}
#         <li><a href="/{{ item.url }}">{{ item.title }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>"""
# tm = Template(link)
# msg = tm.render(path=menu)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]

# cars = [9, 8, 6, 2, 3, 5, 7, 4]
# tpl = "Сумма: {{ cs | sum(attribute='price') }}"
# tpl = "Сумма: {{ (cs | max(attribute='price')).model }}"
# tpl = "Сумма: {{ cs | random}}"
# tpl = "Сумма: {{ cs | replace('price', 'brand')}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# html = """
# {% macro func_input(name, value="", type"text", size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
#
# {% endmacro %}
#
# <p>{{ func_input('username') }}</p>
# <p>{{ func_input('email') }}</p>
# <p>{{ func_input('password'), type="password") }}</p>
#
# """
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


from jinja2 import Environment, FileSystemLoader

# persons = [
#
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#
#     {"name": "Никита", "year": 28, "weight": 82.3},
#
#     {"name": "Виталий", "year": 33, "weight": 94.0}
#
# ]

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title='About Jinja')
#
# print(msg)


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render()

print(msg)