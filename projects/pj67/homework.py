from parsers1 import Parser


def main():
    for i in range(4):
        pars = Parser(f"https://habr.com/ru/articles/page{i}/", "habr_news.txt")
        pars.run()


if __name__ == '__main__':
    main()
