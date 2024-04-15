import os
import unittest
import HtmlTestRunner
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

class TeaMW(unittest.TestCase):
    # Dashboard
    TeaMW_link = "https://fmcasesores.000webhostapp.com/"
    index_title = "TeaMW Dashboard"
    theme_option = "/html/body/div[1]/div[2]/header/div/li/button"
    dashboard_title = "/html/body/div[1]/div[2]/main/div/h2"

    # Employees
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

    # Teams
    teams_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[2]"
    teams_heading = "/html/body/div[1]/div[2]/main/div/h2"
    add_ttitle_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_tleader_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_tdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/textarea"
    add_team_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    edit_team_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[5]/div/a/button"
    team_edit_title_input = "/html/body/form/div/label[1]/input"
    team_edit_save = "/html/body/form/div/div[1]/input"
    team_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[6]/div/a/button"

    # Projects
    projs_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[3]"
    projs_heading = "/html/body/div[1]/div[2]/main/div/h2"
    add_pname_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_pdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/textarea"
    add_proj_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    edit_proj_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[4]/div/a/button"
    proj_edit_name_input = "/html/body/form/div/label[1]/input"
    proj_edit_save = "/html/body/form/div/div[1]/input"
    proj_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[5]/div/a/button"

    # Tasks
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

    # DASHBOARD TESTS

    def test_open_page(self):
        self.open(self.TeaMW_link)
        self.assert_title(self.index_title)

    def test_change_theme(self):
        self.open(self.TeaMW_link)
        self.click(self.theme_option)

    def test_totals(self):
        self.open("https://fmcasesores.000webhostapp.com/index.php")
        self.assert_element(self.dashboard_title)

    def test_pending_tasks(self):
        self.open("https://fmcasesores.000webhostapp.com/index.php")
        self.assert_element(self.dashboard_title)

    # EMPLOYEES TESTS

    def test_see_emps(self):
        self.open(self.TeaMW_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)

    def test_add_emp(self):
        self.open(self.TeaMW_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.send_keys(self.add_name_input, "Jhon")
        self.send_keys(self.add_lname_input, "Miller")
        self.send_keys(self.add_role_input, "Frontend Developer")
        self.send_keys(self.add_email_input, "jhon@gmail.com")
        self.send_keys(self.add_team_input, "Web Dev Team")
        self.click(self.add_emp_btn)

    def test_edit_emp(self):
        self.open(self.TeaMW_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.click(self.emp_edit_btn)
        self.clear(self.emp_edit_name_input)
        self.send_keys(self.emp_edit_name_input, "Mark")
        self.click(self.emp_edit_save)

    def test_delete_emp(self):
        self.open(self.TeaMW_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.click(self.emp_delete_btn)

    # TEAMS TESTS

    def test_see_teams(self):
        self.open(self.TeaMW_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)

    def test_add_team(self):
        self.open(self.TeaMW_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.send_keys(self.add_ttitle_input, "New team")
        self.send_keys(self.add_tleader_input, "Somebody")
        self.send_keys(self.add_tdescription_input, "A team with a function")
        self.click(self.add_team_btn)

    def test_edit_team(self):
        self.open(self.TeaMW_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.click(self.edit_team_btn)
        self.clear(self.team_edit_title_input)
        self.send_keys(self.team_edit_title_input, "Old team")
        self.click(self.team_edit_save)

    def test_delete_team(self):
        self.open(self.TeaMW_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.click(self.team_delete_btn)

    # PROJECTS TESTS

    def test_see_projs(self):
        self.open(self.TeaMW_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)

    def test_add_proj(self):
        self.open(self.TeaMW_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.send_keys(self.add_pname_input, "New project")
        self.send_keys(self.add_pdescription_input, "A project created by somebody")
        self.click(self.add_proj_btn)

    def test_edit_proj(self):
        self.open(self.TeaMW_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.click(self.edit_proj_btn)
        self.clear(self.proj_edit_name_input)
        self.send_keys(self.proj_edit_name_input, "Old project")
        self.click(self.proj_edit_save)

    def test_delete_proj(self):
        self.open(self.TeaMW_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.click(self.proj_delete_btn)

    # TASKS TESTS

    def test_see_tks(self):
        self.open(self.TeaMW_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)

    def test_add_tks(self):
        self.open(self.TeaMW_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.send_keys(self.add_ktitle_input, "New task")
        self.send_keys(self.add_kproject_input, "Belongs to a certain project")
        self.send_keys(self.add_kemp_input, "Assigned to somebody")
        self.click(self.add_tks_btn)

    def test_edit_tks(self):
        self.open(self.TeaMW_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.click(self.tks_edit_btn)
        self.clear(self.tks_edit_title_input)
        self.send_keys(self.tks_edit_title_input, "Old task")
        self.click(self.tks_edit_save)

    def test_delete_tks(self):
        self.open(self.TeaMW_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.click(self.tks_delete_btn)

    def setUp(self):
        # Configura el navegador
        self.driver = Edge()
        self.driver.maximize_window()

    def tearDown(self):
        # Cierra el navegador después de la ejecución de las pruebas
        self.driver.quit()

    def open(self, url):
        self.driver.get(url)

    def assert_title(self, expected_title):
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title)

    def assert_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.assertIsNotNone(element)

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def send_keys(self, locator, text):
        self.driver.find_element(By.XPATH, locator).send_keys(text)

    def clear(self, locator):
        self.driver.find_element(By.XPATH, locator).clear()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
