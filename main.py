# from xlrd import open_workbook
import server1 as server

s = server.Server()
procText = input("Введите текст на Русском: ")
s.Translate(lang='Ru', text=procText)