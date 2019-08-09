# from xlrd import open_workbook
import translater

s = translater.Translater()

def MainMenu():
    procText = input("Введите текст на Русском: ")
    s.Translate(lang='Ru', text=procText)
    command = input("Продолжить?(д/н): ")
    if command == "д":
        MainMenu()
    elif command == "синх":
        pass
    else:
        exit()

MainMenu()