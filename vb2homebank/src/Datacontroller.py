from vb2homebank.src.Depends import *


class VbHomeBaseConverter:

    def __init__(self, filename):
        self.filename = filename

    def vb2homebank(self, outfile):
        dataset_list = []
        with open(self.filename, 'r', encoding="ISO-8859-1") as csvfile:
            read_csv = csv.reader(csvfile, delimiter=';', )
            for row in read_csv:
                if row.__len__() <= 12:
                    continue
                elif row[1] == '':
                    continue
                elif readCSV.line_num >= 15:
                    dataset = Dataset.DataSet(row)
                    dataset_list.append(dataset)
                elif readCSV.line_num < 15:
                    continue
        with open(outfile, 'w') as csvoutfile:
            writer = csv.writer(csvoutfile, delimiter=';')
            for d in dataset_list:
                writer.writerow(d.getHomeBankRowString())


class DataSet:
    # VB:
    # 0=Buchungstag
    # 1=Valuta
    # 2=Zahlungsempfänger
    # 3=Empfänger/Zahlungspflichtiger
    # 4=Konto-Nr.
    # 5=IBAN
    # 6=BLZ
    # 7=BIC
    # 8=Vorgang/Verwendungszweck
    # 9=Kundenreferenz
    # 10=Währung
    # 11=Umsatz
    # 12=""

    def __init__(self,rpw):
        self.money_value = 0.0
        self.date = datetime.date(2000,1,1)
        self.receiver = ""
        self.info = ""
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
        # homebank spec: http://homebank.free.fr/help/index.html
        return [str(self.date), "0", self.info, str(self.receiver), '', str(self.money_value), "Verschiedenes", "tag1"]

