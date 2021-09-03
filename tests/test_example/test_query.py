import os
import unittest

from selenium import webdriver

from covid19_cases.hk_database.helperfunc import *


class Covid_19_query(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(os.getcwd(), "chromedriver.exe"))
        self.driver.get("https://www.worldometers.info/coronavirus/?")

    def test_ok(self):
        assert True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
