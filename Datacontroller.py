from Depends import *

class DataController:

    def __init__(self, filename):
        self.filename = filename

    def splitgooglelocationsbydate(self, startdate, enddate):
        t_start = datetime.datetime(startdate.year, startdate.month, startdate.day, 0, 0).timestamp()
        t_end = datetime.datetime(enddate.year, enddate.month, enddate.day, 0, 0).timestamp()
        out_array = []
        with open(self.filename) as json_file:
            data = json.load(json_file)
            for location in data['locations']:
                ts = float(location['timestampMs']) / 1000
                if t_start <= ts <= t_end:
                    out_array.append(location)
        name = self.filename.split('.')
        outputfilename = name[0] + "_" + startdate.strftime("%d_%m_%y") + "_" + enddate.strftime("%d_%m_%y") + ".json"
        with open(outputfilename, 'w') as outfile:
            json.dump(out_array, outfile)
        print("Created" + outputfilename)

    def vb2homebank(self, outfile):
        datasetList = []
        with open(self.filename, 'r', encoding="ISO-8859-1") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';', )
            for row in readCSV:
                if row.__len__() <= 12:
                    continue
                elif row[1] == '':
                    continue
                elif readCSV.line_num >= 15:
                    dataset = Dataset.DataSet()
                    dataset.parsedata(row)
                    datasetList.append(dataset)
                elif readCSV.line_num < 15:
                    continue
        with open(outfile, 'w') as csvoutfile:
            writer = csv.writer(csvoutfile, delimiter=';')
            for d in datasetList:
                writer.writerow(d.getHomeBankRowString())
