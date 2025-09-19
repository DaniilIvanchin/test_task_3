from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfiniteScrollPage(BasePage):
    URL = "http://the-internet.herokuapp.com/infinite_scroll"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='Infinite Scroll']")
    PARAGRAPHS = (By.XPATH, "//div[@class='jscroll-added']")

    TARGET_PARAGRAPHS = 22
    MAX_SCROLLS = 100

    def get_paragraph_count(self):
        elements = WebDriverWait(self.driver, 0.5).until(
            EC.presence_of_all_elements_located(self.PARAGRAPHS)
        )
        count = len(elements)
        self.logger.info(f"Текущее количество абзацев на странице: {count}")
        return count

    def scroll_down(self, pixels=800):
        self.logger.info(f"Скроллим страницу на {pixels} пикселей")
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def ensure_paragraphs_loaded(self):
        count = self.get_paragraph_count()
        self.logger.info(f"Начинаем подгрузку абзацев до {self.TARGET_PARAGRAPHS} элементов")

        for i in range(1, self.MAX_SCROLLS + 1):
            if count >= self.TARGET_PARAGRAPHS:
                self.logger.info(f"Достигнуто целевое количество абзацев: {count}")
                return True

            self.logger.info(f"Попытка #{i}: текущие абзацы = {count}")
            self.scroll_down()

            try:
                WebDriverWait(self.driver, 0.5).until(
                    lambda d: self.get_paragraph_count() > count
                )
                count = self.get_paragraph_count()
                self.logger.info(f"Появились новые абзацы: {count}")
            except:
                self.logger.warning("Новые абзацы не появились на этой итерации")

        self.logger.warning(f"Не удалось загрузить целевое количество абзацев после {self.MAX_SCROLLS} попыток")
        return count >= self.TARGET_PARAGRAPHS
