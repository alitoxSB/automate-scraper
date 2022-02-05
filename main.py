import colorama
from colorama import Fore
from ui.msg import menu_art, ingle_msg
from twitterScraper.twits_scraper import searching
from sentimental_analysis.text_processing import start_system
import pandas as pd
# --------Configure-----------
from twint.twint import Config, run
c = Config()
colorama.init(autoreset=True)

if __name__ == '__main__':
    option = 0
    while option!=3:
        ingle_msg()
        option = int(input('Select a option: '))
        if option == 1:
            try:
                searching()
            except:
                print("Sorry, we have a problem!")
        elif (option==2):
            try:
                start_system()
                print("...")
            except:
                print("Sorry, we have a problem!")