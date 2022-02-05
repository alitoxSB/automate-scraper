import colorama
from colorama import Fore
from ui.msg import menu_art, ingle_msg
from sentimental_analysis.text_processing import start_system
import pandas as pd
# --------Configure-----------
from twint.twint import Config, run
c = Config()
colorama.init(autoreset=True)

def searching():
    """
        function for start searching words on twitter.
    """
    menu_art()
    first_word = input(f"{Fore.RED}Write word for search in Twitter: ")
    option = int(input('You need other word in tweet to scraping? 1: Yes or 2: No '))
    if (option == 1):
        second_word = input(f"{Fore.RED}Write second word for search in Twitter: ")
        c.Search = first_word + "\"" + second_word + "\""
    else:
        pass
    c.Search = first_word+ "\""
    c.Retweets = True
    c.Store_json = True
    c.User_full = True
    c.Store_csv = True
    c.Output = "data.csv"

    print(f"{Fore.RED}Since date do you want in Twitter?")
    print(f"{Fore.RED}Enter date like this: Year: 2021, Month: 01, Day: 01")
    year = input(f"{Fore.RED}Year: ")
    month = input(f"{Fore.RED}Month: ")
    day = input(f"{Fore.RED}Day: ")
    since = year+"-"+month+"-"+day+" "+"00:00:00"
    c.Since = since
    run.Search(c)

    df = pd.read_csv('data.csv')
    index = df.tweet.index
    number_of_rows = len(index)
    print(number_of_rows, " Tweets scraped")