from parsers1 import Parser


def main():
    for i in range(11):
        pars = Parser(f"https://www.ixbt.com/live/index/news/page{i}", "news1.txt")
        pars.run()


if __name__ == '__main__':
    main()
