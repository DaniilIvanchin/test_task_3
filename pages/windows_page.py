from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WindowsPage(BasePage):
    URL = "http://the-internet.herokuapp.com/windows"
    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='Opening a new window']")
    LINK = (By.XPATH, "//a[text()='Click Here']")
    NEW_WINDOW_TEXT = (By.XPATH, "//h3[text()='New Window']")

    def click_link(self):
        self.logger.info("Кликаем по ссылке 'Click Here'")
        self.wait.until(EC.element_to_be_clickable(self.LINK)).click()

    def switch_to_tab(self, index):
        handles = self.driver.window_handles
        self.logger.info(f"Переключаемся на вкладку #{index}, всего вкладок: {len(handles)}")
        self.driver.switch_to.window(handles[index])

    def get_tab_title(self):
        title = self.driver.title
        self.logger.info(f"Текущий заголовок вкладки: '{title}'")
        return title

    def get_new_window_text(self):
        text = self.wait.until(EC.visibility_of_element_located(self.NEW_WINDOW_TEXT)).text
        self.logger.info(f"Текст на новой вкладке: '{text}'")
        return text

    def close_current_tab(self):
        self.logger.info(f"Закрываем текущую вкладку '{self.driver.title}'")
        self.driver.close()
