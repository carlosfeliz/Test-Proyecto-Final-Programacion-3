import os
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner

class DashboardTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = Service(r"C:\Program Files (x86)\msedgedriver.exe")
        cls.driver = webdriver.Edge(service=cls.service)
        cls.driver.maximize_window()

    def test_open_page(self):
        self.driver.get("https://fmcasesores.000webhostapp.com/")
        self.assertIn("TeaMW", self.driver.title)  # Modificación aquí
        self.take_screenshot("open_page")

    def test_change_theme(self):
        self.driver.get("https://fmcasesores.000webhostapp.com/")
        theme_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div/li/button")
        theme_button.click()
        self.take_screenshot("change_theme")

    def test_totals(self):
        self.driver.get("https://fmcasesores.000webhostapp.com/index.php")
        self.assertIn("TeaMW", self.driver.title)  # Modificación aquí
        self.take_screenshot("totals")

    def test_pending_tasks(self):
        self.driver.get("https://fmcasesores.000webhostapp.com/index.php")
        self.assertIn("TeaMW", self.driver.title)  # Modificación aquí
        self.take_screenshot("pending_tasks")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def take_screenshot(self, name):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
