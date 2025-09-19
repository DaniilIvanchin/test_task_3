from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='Dynamic Content']")
    IMAGE_LOCATORS = (By.XPATH, "//div[@class='large-2 columns']/img")

    def get_images_src(self):
        self.logger.info("Получаем все изображения на странице")
        images = self.wait.until(EC.presence_of_all_elements_located(self.IMAGE_LOCATORS))
        src_list = [img.get_attribute("src") for img in images]
        self.logger.info(f"Собран список src изображений: {src_list}")
        return src_list

    def reload_until_match(self, max_attempts=20):
        self.logger.info(f"Пробуем обновлять страницу до {max_attempts} раз, чтобы найти дубли изображений")

        for attempt in range(1, max_attempts + 1):
            self.logger.info(f"Попытка #{attempt}")
            src_list = self.get_images_src()
            if len(src_list) != len(set(src_list)):
                self.logger.info("Найдены дубли изображений, условие выполнено")
                return True
            self.logger.info("Дубли не найдены, обновляем страницу")
            self.driver.refresh()

        self.logger.warning("Условие не выполнено после всех попыток")
        return False