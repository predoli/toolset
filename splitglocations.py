from Datacontroller import *

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", help="DD-MM-YYYY")
parser.add_argument("-e", "--end", help="DD-MM-YYYY")
parser.add_argument("filename")
args = parser.parse_args()

if args.start:
    dateplit = args.start.split("-")
    startdate = datetime.datetime(int(dateplit[2]), int(dateplit[1]), int(dateplit[0]))
else:
    startdate = datetime.datetime(1970, 1, 1)

if args.end:
    dateplit = args.end.split("-")
    enddate = datetime.datetime(int(dateplit[2]), int(dateplit[1]), int(dateplit[0]))
else:
    enddate = datetime.datetime.now()

c = DataController(args.filename)
c.splitgooglelocationsbydate(startdate, enddate)

