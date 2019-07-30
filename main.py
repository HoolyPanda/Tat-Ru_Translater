# from xlrd import open_workbook
import server1 as server

s = server.Server()

def MainMenu():
    procText = input("Введите текст на Русском: ")
    s.Translate(lang='Ru', text=procText)
    command = input("Продолжить?(д/н): ")
    if command == "д":
        MainMenu()
    else:
        exit()

MainMenu()