from Datacontroller import *

parser = argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("outfile")
args = parser.parse_args()


c = DataController(args.infile)
c.vb2homebank(args.outfile)

