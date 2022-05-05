import datetime


def main():
    dt = datetime.datetime.now() + datetime.timedelta(hours=9)
    print(dt.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    main()
