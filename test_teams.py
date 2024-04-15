import os
import unittest
import HtmlTestRunner
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

class Teams(unittest.TestCase):

    TeaMW_link = "https://fmcasesores.000webhostapp.com/"

    # See
    teams_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[2]"
    teams_heading = "/html/body/div[1]/div[2]/main/div/h2"

    # Add
    add_ttitle_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_tleader_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_tdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/textarea"
    add_team_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"

    # Edit
    edit_team_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[5]/div/a/button"
    team_edit_title_input = "/html/body/form/div/label[1]/input"
    team_edit_save = "/html/body/form/div/div[1]/input"

    # Delete
    team_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[6]/div/a/button"

    @classmethod
    def setUpClass(cls):
        cls.driver = Edge()
        cls.driver.maximize_window()

    def test_see_teams(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.teams_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.teams_heading).is_displayed())
     
        # self.save_screenshot("see_teams_sc")

    def test_add_team(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.teams_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.teams_heading).is_displayed())
        self.driver.find_element(By.XPATH, self.add_ttitle_input).send_keys("New team")
        self.driver.find_element(By.XPATH, self.add_tleader_input).send_keys("Somebody")
        self.driver.find_element(By.XPATH, self.add_tdescription_input).send_keys("A team with a function")
        self.driver.find_element(By.XPATH, self.add_team_btn).click()
       
        # self.save_screenshot("add_team_sc")

    def test_edit_team(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.teams_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.teams_heading).is_displayed())
      
        self.driver.find_element(By.XPATH, self.edit_team_btn).click()
        self.driver.find_element(By.XPATH, self.team_edit_title_input).clear()
        self.driver.find_element(By.XPATH, self.team_edit_title_input).send_keys("Old team")
        self.driver.find_element(By.XPATH, self.team_edit_save).click()
        # self.save_screenshot("edit_team_sc")

    def test_delete_team(self):
        self.driver.get(self.TeaMW_link)
        self.driver.find_element(By.XPATH, self.teams_menu_opt).click()
        self.assertTrue(self.driver.find_element(By.XPATH, self.teams_heading).is_displayed())
     
        self.driver.find_element(By.XPATH, self.team_delete_btn).click()
        # self.save_screenshot("delete_team_sc")

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
