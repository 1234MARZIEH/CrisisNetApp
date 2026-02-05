
import argparse
from core import adaptive_download

parser = argparse.ArgumentParser(description="CrisisNet Downloader")
parser.add_argument("--url", required=True)
parser.add_argument("--out", required=True)
parser.add_argument("--crisis", action="store_true")

args = parser.parse_args()

delay = 1.5 if args.crisis else 0.3
adaptive_download(args.url, args.out, delay=delay)

print("Finished.")
input("Press Enter to exit...")

