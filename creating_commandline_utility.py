import argparse
parser=argparse.ArgumentParser()
parser.add_argument("Url",help="Url of the file to download")
parser.add_argument("output",help="by which name you want to save your file")
args=parser.parse_args()
print(args.Url)
print(args.output)
