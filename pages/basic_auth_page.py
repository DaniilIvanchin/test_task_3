from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasicAuthPage(BasePage):
    URL = "https://the-internet.herokuapp.com/basic_auth"
    USER_NAME = "admin"
    USER_PASSWORD = "admin"
    TEXT_LOCATOR = (By.XPATH, "//div[@class='example']/p")
    SUCCESS_TEXT = "Congratulations! You must have the proper credentials."

    def open_with_auth(self):
        auth_url = self.URL.replace("https://", f"https://{self.USER_NAME}:{self.USER_PASSWORD}@")
        self.driver.get(auth_url)

    def get_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.TEXT_LOCATOR)).text

    def get_page_text(self):
        self.logger.info("Получаем текст с элемента")
        element = self.wait.until(EC.visibility_of_element_located(self.TEXT_LOCATOR))
        return element.text.strip() == self.SUCCESS_TEXT