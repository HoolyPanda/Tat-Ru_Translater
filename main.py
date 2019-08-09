# from xlrd import open_workbook
import translater
import client

s = translater.Translater()

def MainMenu():
    # client.Client().PushDict()
    procText = input("Введите текст на Русском: ")
    # client.Client().PullDict()
    s.Translate(lang='Ru', text=procText)
    command = input("Продолжить?(д/н): ")
    if command == "д":
        MainMenu()
    elif command == "синх":
        command = input('загр/скач?: ')
        if command == "загр":
            client.Client().PushDict()
        elif command == "скач":
            client.Client().PullDict()
        pass
    else:
        exit()

MainMenu()