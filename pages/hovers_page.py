from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HoversPage(BasePage):
    URL = "https://the-internet.herokuapp.com/hovers"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='Hovers']")
    USER_BOXES = (By.XPATH, "//div[@class='figure']")
    NOT_FOUND_TITLE = (By.XPATH, "//h1[text()='Not Found']")

    LOCATOR_TYPE = By.XPATH
    USER_LOCATOR_TEMPLATE = "(//div[@class='figure'])[{}]"
    PROFILE_LINK_TEMPLATE = "(//div[@class='figure'])[{}]//a[contains(text(),'View profile')]"

    def get_user_count(self):
        self.logger.info("Пробуем найти все элементы пользователей")
        users = self.wait.until(
            EC.presence_of_all_elements_located((self.USER_BOXES))
        )
        count = len(users)
        self.logger.info(f"Количество найденных пользователей: {count}")
        return count

    def hover_user_and_open_profile(self, index: int):
        user_locator = (self.LOCATOR_TYPE, self.USER_LOCATOR_TEMPLATE.format(index + 1))
        profile_link_locator = (self.LOCATOR_TYPE, self.PROFILE_LINK_TEMPLATE.format(index + 1))

        self.logger.info(f"Наводим курсор на пользователя №{index + 1}")
        user = self.wait.until(EC.presence_of_element_located(user_locator))
        ActionChains(self.driver).move_to_element(user).perform()

        self.logger.info(f"Кликаем по ссылке профиля пользователя №{index + 1}")
        self.wait.until(EC.element_to_be_clickable(profile_link_locator)).click()

        self.logger.info("Проверяем, что открылась страница Not Found")
        self.wait.until(EC.visibility_of_element_located((self.NOT_FOUND_TITLE)))

        self.logger.info("Возврат назад на страницу Hovers")
        self.driver.back()
        self.is_opened()

        self.logger.info("Действие hover + переход в профиль успешно завершено")
        return True
