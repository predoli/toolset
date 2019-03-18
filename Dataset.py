import datetime
import csv


class DataSet:
    def __init__(self):
        self.money_value = 0.0
        self.date = datetime.date(2000,1,1)
        self.receiver = ""
        self.info = ""

    def parsedata(self, row):
        self.dataparser(row)

    def moneyhandler(self, moneystr, signstr):
        if moneystr.find(".") != -1:
            moneystr = moneystr.replace('.', '')
        value = float(moneystr.replace(',', '.'))
        if (signstr == 'S'):
            self.money_value = value * -1
        else:
            self.money_value = value

    def datehandler(self, datestr):
        datestrlist = (datestr.split("."))
        self.date = datetime.date(int(datestrlist[2]), int(datestrlist[1]), int(datestrlist[0]))

    def dataparser(self, rowlist):
        self.datehandler(rowlist[1])
        self.moneyhandler(rowlist[11], rowlist[12])
        self.receiver = rowlist[3]
        self.info = rowlist[8]

    def getHomeBankRowString(self):
        return [str(self.date), "0", "", str(self.receiver), '', str(self.money_value), "Verschiedenes", "tag1"]





