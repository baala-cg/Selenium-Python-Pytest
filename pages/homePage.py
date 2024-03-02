from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_css = "[class='oxd-userdropdown-name']"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.CSS_SELECTOR, self.welcome_link_css).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()