import os
import unittest
import HtmlTestRunner
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

class Projects(unittest.TestCase):

    TeaMW_link = "https://fmcasesores.000webhostapp.com/"
    
    projs_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[3]"
    projs_heading = "/html/body/div[1]/div[2]/main/div/h2"

    add_pname_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_pdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/textarea"
    add_proj_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    
    edit_proj_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[4]/div/a/button"
    proj_edit_name_input = "/html/body/form/div/label[1]/input"
    proj_edit_save = "/html/body/form/div/div[1]/input"
    
    proj_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[5]/div/a/button"

    @classmethod
    def setUpClass(cls):
        cls.driver = Edge()
        cls.driver.maximize_window()

    def test_see_projs(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.projs_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.projs_heading).is_displayed())
        self.save_screenshot("see_projs_sc")

    def test_add_proj(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.projs_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.projs_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.add_pname_input).send_keys("New project")
        self.driver.find_element(By.XPATH, self.add_pdescription_input).send_keys("A project created by somebody")
        self.driver.find_element(By.XPATH, self.add_proj_btn).click()
        self.save_screenshot("add_proj_sc")

    def test_edit_proj(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.projs_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.projs_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.edit_proj_btn).click()
        self.driver.find_element(By.XPATH, self.proj_edit_name_input).clear()
        self.driver.find_element(By.XPATH, self.proj_edit_name_input).send_keys("Old project")
        self.driver.find_element(By.XPATH, self.proj_edit_save).click()
        self.save_screenshot("edit_proj_sc")

    def test_delete_proj(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.projs_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.projs_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.proj_delete_btn).click()
        self.save_screenshot("delete_proj_sc")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def save_screenshot(self, name):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
