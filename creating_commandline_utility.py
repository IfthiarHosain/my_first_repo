import argparse
import requests
def download_file(Url,local_filename):
    with requests.get(Url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename,"wb") as f:
            for chunk in r.iter_content(cjhunk_size=8192):
                f.write(chunk)
    return local_filename
parser=argparse.ArgumentParser()
parser.add_argument("Url",help="Url of the file to download")
parser.add_argument("output",help="by which name you want to save your file")
args=parser.parse_args()
print(args.Url)
print(args.output)
download_file(args.Url,args.output)