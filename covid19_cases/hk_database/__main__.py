import os
import time
import traceback

import click
from selenium import webdriver

from covid19_cases.hk_database.helperfunc import *

URL = "https://www.worldometers.info/coronavirus/?"


@click.command()
@click.option(
    "-w",
    "--webdriver_path",
    help="Path of webdriver used to load URL.",
    default=os.path.join(os.getcwd(), "chromedriver.exe"),
)
@click.option(
    "-l",
    "--location",
    help="Target location to get COVID-19 cases report",
    default="Hong Kong",
)
@click.option(
    "-d",
    "--dir",
    "dir",
    help="Directory to save output data.",
    default=os.getcwd(),
)
def start_scraping(webdriver_path, location, dir):
    with webdriver.Chrome(webdriver_path) as wd:
        wd.get(URL)
        try:
            df = get_cases_tdy_by_loc(wd, location)
            exported_path = export(df, location, dir)

        except:
            traceback.print_exc()


if __name__ == "__main__":
    start_time = time.time()
    start_scraping()
    print("--- %s seconds ---" % (time.time() - start_time))
