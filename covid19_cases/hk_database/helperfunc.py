import os
from datetime import date

import pandas as pd
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_cases_tdy_by_loc(driver, location):
    """Get_cases_tdy_by_loc returns a DataFrame that reports covid-19 cases today of the target location."""
    # Locate the search button and inputs the target location
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    search = driver.find_element_by_css_selector("input[type='search']")
    search.clear()
    search.send_keys(location)
    search.send_keys(Keys.RETURN)
    # Click the 'Now' button the get cases today
    now_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Now"))
    )
    now_button.click()
    # Retrieve a DataFrame with covid-19 cases today of target location by parsing html
    html = driver.page_source
    df = pd.read_html(html)[0]
    return df


def export(df, location, dir):
    """This function exports the scraped data into location.csv file.
    If location.xlsx does not exist, append to the existing excel file otherwise."""
    # replace first column by date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    hk_df = df.iloc[[0]].copy()
    hk_df.iloc[:, 0] = d

    # name the file name by location
    filename = f"{location}.csv"
    export_path = os.path.join(dir, filename)

    if not os.path.isfile(export_path):
        hk_df.to_csv(export_path, index=False)
    elif d not in hk_df.iloc[:, 0].values:
        hk_df.to_csv(export_path, mode="a", header=False, index=False)
    return export_path
