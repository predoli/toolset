from src.Depends import *


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
                elif read_csv.line_num >= 15:
                    dataset = DataSet(row)
                    dataset_list.append(dataset)
                elif read_csv.line_num < 15:
                    continue
        with open(outfile, 'w') as csvoutfile:
            writer = csv.writer(csvoutfile, delimiter=';')
            for d in dataset_list:
                writer.writerow(d.get_home_bank_row_string())


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

    def __init__(self,row):
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
        self.info = " ".join(rowlist[8].split())

    def get_home_bank_row_string(self):
        # homebank spec: http://homebank.free.fr/help/index.html
        # 15-02-04;0;;;Some cash;-40,00;Bill:Withdrawal of cash;tag1 tag2
        # 15-02-04;1;;;Internet DSL;-45,00;Inline service/Internet;tag2 my-tag3
        return [str(self.date), "0", "", str(self.receiver), self.info, str(self.money_value), "Verschiedenes", "tag1"]


