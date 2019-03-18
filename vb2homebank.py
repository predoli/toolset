from Datacontroller import *

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="input file name (.csv)")
parser.add_argument("outfile", help="output file name (.csv)")
args = parser.parse_args()


c = DataController(args.infile)
c.vb2homebank(args.outfile)

