from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    URL = "https://the-internet.herokuapp.com/context_menu"
    HOTSPOT_LOCATOR = (By.ID, "hot-spot")
    ALERT_TEXT = "You selected a context menu"
    CHECK_PAGE_LOCATOR = (By.ID, "hot-spot")

    def trigger_context_menu(self):
        hotspot = self.wait.until(EC.presence_of_element_located(self.HOTSPOT_LOCATOR))
        if self.logger:
            self.logger.info("Нашёл hotspot для клика правой кнопкой")

        ActionChains(self.driver).context_click(hotspot).perform()
        if self.logger:
            self.logger.info("Выполнил клик правой кнопкой мыши по hotspot")

        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        if self.logger:
            self.logger.info(f"Появился alert с текстом: '{text}'")

        assert text == self.ALERT_TEXT
        if self.logger:
            self.logger.info("Текст alert совпадает с ожидаемым")

        alert.accept()
        if self.logger:
            self.logger.info("Закрыл alert (нажал OK)")

        return True
