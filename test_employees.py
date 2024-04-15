import os
import unittest
from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import HtmlTestRunner

class Employees(unittest.TestCase):

    TeaMW_link = "https://fmcasesores.000webhostapp.com/"
    emp_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[1]"
    emp_heading = "/html/body/div[1]/div[2]/main/div/h2"
    add_name_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_lname_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_role_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/input"
    add_email_input = "/html/body/div[1]/div[2]/main/div/form/div/label[4]/input"
    add_team_input = "/html/body/div[1]/div[2]/main/div/form/div/label[5]/input"
    add_emp_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    emp_edit_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr[1]/td[7]/div/a/button"
    emp_edit_name_input = "/html/body/form/div/label[1]/input"
    emp_edit_save = "/html/body/form/div/div[1]/input"
    emp_delete_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr[1]/td[8]/div/a/button"

    @classmethod
    def setUpClass(cls):
        cls.service = Service(r"C:\Program Files (x86)\msedgedriver.exe")
        cls.driver = Edge(service=cls.service)
        cls.driver.maximize_window()

    def test_see_emps(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.emp_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.emp_heading).is_displayed())
        self.save_screenshot("see_emps_sc")

    def test_add_emp(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.emp_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.emp_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.add_name_input).send_keys("Jhon")
        self.driver.find_element(By.XPATH, self.add_lname_input).send_keys("Miller")
        self.driver.find_element(By.XPATH, self.add_role_input).send_keys("Frontend Developer")
        self.driver.find_element(By.XPATH, self.add_email_input).send_keys("jhon@gmail.com")
        self.driver.find_element(By.XPATH, self.add_team_input).send_keys("Web Dev Team")
        self.driver.find_element(By.XPATH, self.add_emp_btn).click()
        self.save_screenshot("add_emp_sc")

    def test_edit_emp(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.emp_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.emp_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.emp_edit_btn).click()
        self.driver.find_element(By.XPATH, self.emp_edit_name_input).clear()
        self.driver.find_element(By.XPATH, self.emp_edit_name_input).send_keys("Mark")
        self.driver.find_element(By.XPATH, self.emp_edit_save).click()
        self.save_screenshot("edit_emp_sc")

    def test_delete_emp(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.emp_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.emp_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.emp_delete_btn).click()
        self.save_screenshot("delete_emp_sc")

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
