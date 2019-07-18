# from xlrd import open_workbook
import server

s = server.Server()
procText = input("Введите текст на Русском: ")
s.Translate(lang='Ru', word=procText)