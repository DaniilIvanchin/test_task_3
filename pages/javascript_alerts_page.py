from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import string
import random

class JavaScriptAlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    RESULT_LOCATOR = (By.ID, "result")
    JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    ALERT_TEXT = "I am a JS Alert"
    CONFIRM_TEXT = "I am a JS Confirm"
    PROMPT_TEXT = "I am a JS prompt"
    CHECK_PAGE_LOCATOR = (By.XPATH, "//button[text()='Click for JS Alert']")

    def click_js_alert(self):
        self.logger.info("Нажимаем кнопку для JS Alert")
        self.wait.until(EC.element_to_be_clickable(self.JS_ALERT_BTN)).click()
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Текст алерта: {text}")
        alert.accept()
        return text == self.ALERT_TEXT

    def click_js_confirm(self):
        self.logger.info("Нажимаем кнопку для JS Confirm")
        self.wait.until(EC.element_to_be_clickable(self.JS_CONFIRM_BTN)).click()
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Текст алерта: {text}")
        alert.accept()
        return text == self.CONFIRM_TEXT

    def click_js_prompt(self):
        self.logger.info("Нажимаем кнопку для JS Prompt")
        self.wait.until(EC.element_to_be_clickable(self.JS_PROMPT_BTN)).click()

        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Текст алерта: {text}")
        assert text == self.PROMPT_TEXT

        random_number = ''.join(random.choices(string.digits, k=6))
        self.logger.info(f"Вводим в prompt: {random_number}")

        alert.send_keys(random_number)
        alert.accept()

        result = self.wait.until(EC.visibility_of_element_located(self.RESULT_LOCATOR)).text
        self.logger.info(f"Результат: {result}")
        assert result == f"You entered: {random_number}"

        return True


class JavaScriptAlertsPageJS(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    RESULT_LOCATOR = (By.ID, "result")
    ALERT_TEXT = "I am a JS Alert"
    CONFIRM_TEXT = "I am a JS Confirm"
    PROMPT_TEXT = "I am a JS prompt"
    CHECK_PAGE_LOCATOR = (By.XPATH, "//button[text()='Click for JS Alert']")
    def js_alert(self):
        self.logger.info("Генерируем JS alert через execute_script")
        self.driver.execute_script(
            f"alert('{self.ALERT_TEXT}'); "
            f"window.addEventListener('unload', function(){{}}); "
            f"document.getElementById('result').innerText = 'You successfully clicked an alert';"
        )
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Алерт появился с текстом: {text}")
        alert.accept()

        result = self.wait.until(EC.visibility_of_element_located(self.RESULT_LOCATOR)).text
        self.logger.info(f"Результат: {result}")
        assert result == "You successfully clicked an alert"
        return text == self.ALERT_TEXT

    def js_confirm(self):
        self.logger.info("Генерируем JS confirm через execute_script")
        self.driver.execute_script(
            f"confirm('{self.CONFIRM_TEXT}'); "
            f"document.getElementById('result').innerText = 'You clicked: Ok';"
        )
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Confirm текст: {text}")
        alert.accept()

        result = self.wait.until(EC.visibility_of_element_located(self.RESULT_LOCATOR)).text
        self.logger.info(f"Результат: {result}")
        assert result == "You clicked: Ok"
        return text == self.CONFIRM_TEXT

    def js_prompt(self):
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.logger.info(f"Генерируем JS prompt с вводом текста: {random_text}")
        self.driver.execute_script(
            f"prompt('{self.PROMPT_TEXT}'); "
            f"document.getElementById('result').innerText = 'You entered: {random_text}';"
        )

        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Prompt текст: {text}")
        assert text == self.PROMPT_TEXT

        alert.send_keys(random_text)
        alert.accept()

        result = self.wait.until(EC.visibility_of_element_located(self.RESULT_LOCATOR)).text
        self.logger.info(f"Результат: {result}")
        assert result == f"You entered: {random_text}"
        return True