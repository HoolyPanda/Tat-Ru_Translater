import csv 
from xlrd import open_workbook
import server


s = server.Server()
s.Translate(lang='Ru', word='великий брат.')
a = server.stem()
v = a.analyze("моего великого брата. jkjkjk")

b = v[0].get("analysis")[0].get('lex')

с = v[2].get("analysis")[0].get('lex')


d = v[4].get("analysis")[0].get('lex')

n = a.lemmatize("моего")
print ("fsd")