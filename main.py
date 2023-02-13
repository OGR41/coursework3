from utils import get_data, get_filter_data



def main():
    DATA = 'https://www.jsonkeeper.com/b/1IUI'
    data, info = get_data(DATA)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filter_data(data)


if __name__ == "__main__":
    main()

