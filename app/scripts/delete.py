import argparse
import os
import sys

sys.path.append(os.path.abspath("."))
from db import Database
from file import File

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url")
    args = parser.parse_args()

    Database.initialise()
    file = File()
    file.delete_by_url(args.url)
