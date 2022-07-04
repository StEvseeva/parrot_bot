from parrot_bot.DB import add_parrot_type


def start():
    img = input()
    add_parrot_type(img)
    print("Parrot's type added!")


if __name__ == '__main__':
    start()
