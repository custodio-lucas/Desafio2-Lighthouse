import sys
import pandas as pd
from asyncore import read
from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args

def main():
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        try:
            csv = read_csv(user_args.csv)
        except ValueError:
            print("Faltou URL ou CSV cara")
            sys.exit(1)
        _site_check(csv)
    _site_check(urls)
    '''user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Faltou URL cara")
        sys.exit(1)
    _site_check(urls)'''

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

def read_csv(csvfile):
    #Read csv file
    df = pd.read_csv(csvfile)
    return list(df)

if __name__ == "__main__":
    main()
