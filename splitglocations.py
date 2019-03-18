from Datacontroller import *

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", help="DD-MM-YYYY")
parser.add_argument("-e", "--end", help="DD-MM-YYYY")
parser.add_argument("filename")
args = parser.parse_args()

if args.start:
    dateplit = args.start.split("-")
    startdate = datetime.date(int(dateplit[2]), int(dateplit[1]), int(dateplit[0]))
else:
    startdate = datetime.date(1970, 1, 1)

if args.end:
    dateplit = args.start.split("-")
    enddate = datetime.date(int(dateplit[2]), int(dateplit[1]), int(dateplit[0]))
else:
    enddate = datetime.date.today()

c = DataController(args.filename)
c.splitgooglelocationsbydate(startdate, enddate)

