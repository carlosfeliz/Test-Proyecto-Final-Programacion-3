import os
import unittest
import HtmlTestRunner
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

class Tasks(unittest.TestCase):

    TeaMW_link = "https://fmcasesores.000webhostapp.com/"

    @classmethod
    def setUpClass(cls):
        cls.driver = Edge()
        cls.driver.maximize_window()

    def test_see_tks(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.tks_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.tks_heading).is_displayed())
        self.save_screenshot("see_tks_sc")

    def test_add_tks(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.tks_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.tks_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.add_ktitle_input).send_keys("New task")
        self.driver.find_element(By.XPATH, self.add_kproject_input).send_keys("Belongs to a certain project")
        self.driver.find_element(By.XPATH, self.add_kemp_input).send_keys("Assigned to somebody")
        self.driver.find_element(By.XPATH, self.add_tks_btn).click()
        self.save_screenshot("add_tks_sc")

    def test_edit_tks(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.tks_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.tks_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.tks_edit_btn).click()
        self.driver.find_element(By.XPATH, self.tks_edit_title_input).clear()
        self.driver.find_element(By.XPATH, self.tks_edit_title_input).send_keys("Old task")
        self.driver.find_element(By.XPATH, self.tks_edit_save).click()
        self.save_screenshot("edit_tks_sc")

    def test_delete_tks(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.tks_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.tks_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.tks_delete_btn).click()
        self.save_screenshot("delete_tks_sc")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def save_screenshot(self, name):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)

    # XPaths for the elements used in the tests
    tks_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[4]"
    tks_heading = "/html/body/div[1]/div[2]/main/div/h2"
    add_ktitle_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_kproject_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_kemp_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/input"
    add_tks_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    tks_edit_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr/td[6]/div/a/button"
    tks_edit_title_input = "/html/body/form/div/label[1]/input"
    tks_edit_save = "/html/body/form/div/div[1]/input"
    tks_delete_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr/td[7]/div/a/button"

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
