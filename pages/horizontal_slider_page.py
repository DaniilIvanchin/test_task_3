import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class HorizontalSliderPage(BasePage):
    URL = "https://the-internet.herokuapp.com/horizontal_slider"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//div[@class='sliderContainer']")
    SLIDER = (By.XPATH, "//input[@type='range']")
    VALUE = (By.ID, "range")

    MIN_VALUE = 0.0
    MAX_VALUE = 5.0
    STEP = 0.5

    def set_random_slider_value(self):
        slider = self.wait.until(EC.element_to_be_clickable(self.SLIDER))
        self.logger.info("Слайдер найден и доступен для взаимодействия")

        values = [round(x * self.STEP, 1)
                  for x in range(int(self.MIN_VALUE / self.STEP), int(self.MAX_VALUE / self.STEP) + 1)]
        target_value = random.choice([v for v in values if v not in (self.MIN_VALUE, self.MAX_VALUE)])
        self.logger.info(f"Случайное целевое значение для слайдера: {target_value}")

        slider.click()
        self.logger.info("Клик по слайдеру")

        slider.send_keys(Keys.HOME, Keys.ARROW_RIGHT * int(target_value / self.STEP))
        self.logger.info(f"Передвинули слайдер до {target_value}")

        value_text = self.wait.until(EC.visibility_of_element_located(self.VALUE)).text
        self.logger.info(f"Текущее значение слайдера отображается как: {value_text}")

        assert float(value_text) == float(target_value)
        self.logger.info("Слайдер установлен корректно")

        return True
