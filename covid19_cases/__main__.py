import os
import time
import traceback

import click
from selenium import webdriver

from covid19_cases.helperfunc import *

URL = "https://www.worldometers.info/coronavirus/?"


@click.command()
@click.option(
    "-w",
    "--webdriver_path",
    prompt="Enter path of webdriver",
    help="Path of webdriver used to load URL.",
    required=True,
    default=os.path.join(os.getcwd(), "chromedriver.exe"),
)
@click.option(
    "-l",
    "--location",
    prompt="Enter target location",
    help="Target location to get COVID-19 cases report",
    required=True,
    default="Hong Kong",
)
@click.option(
    "-d",
    "--dir",
    "dir",
    prompt="Enter save directory path",
    help="Directory to save output data.",
    required=False,
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
