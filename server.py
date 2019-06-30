from pandas import ExcelFile
from pandas import ExcelWriter
import pandas

class Server:
    def __init__(self):
        self.wordlist = pandas.read_excel("tato-wordlist.xlsx" , sheet_name='Русский - Тато')
        print(self.wordlist['Слово'][1])
        self.wl = self.wordlist['Слово']
        pass
    def Translate(self, RuWord:str):
        for wordIndex in self.wordlist.index:
            if (self.wl[wordIndex] == RuWord):
                print(self.wordlist['Перевод'][wordIndex]) 
                pass