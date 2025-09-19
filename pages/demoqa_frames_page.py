from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FramesPage(BasePage):
    URL = "https://demoqa.com/frames"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h1[@class='text-center']")
    ALERTS_MENU = (By.XPATH, "//div[contains(text(), 'Alerts, Frame')]")
    NESTED_FRAMES_MENU = (By.XPATH, "//span[text()='Nested Frames']")
    FRAMES_MENU = (By.XPATH, "//span[text()='Frames']")
    MENU_BLOCK = (By.XPATH, "//div[contains(@class, 'element-list')]")

    PARENT_FRAME = (By.ID, "frame1")
    CHILD_FRAME = (By.TAG_NAME, "iframe")
    PARENT_BODY = (By.XPATH, "//body")
    CHILD_PARAGRAPH = (By.XPATH, "//p")

    FRAME1 = (By.ID, "frame1")
    FRAME2 = (By.ID, "frame2")
    FRAME_HEADING = (By.ID, "sampleHeading")

    PARENT_TEXT = "Parent frame"
    CHILD_TEXT = "Child Iframe"

    def ensure_menu_open(self):
        self.logger.info("Проверяем, открыт ли блок меню")
        block = self.wait.until(EC.presence_of_element_located(self.MENU_BLOCK))
        if "show" not in block.get_attribute("class"):
            self.logger.info("Блок меню закрыт, кликаем по 'Alerts, Frame & Windows'")
            menu = self.wait.until(EC.element_to_be_clickable(self.ALERTS_MENU))
            self.driver.execute_script("arguments[0].click();", menu)

    def go_to_nested_frames(self):
        self.logger.info("Переходим в меню Nested Frames")
        nested_menu = self.wait.until(EC.presence_of_element_located(self.NESTED_FRAMES_MENU))
        self.driver.execute_script("arguments[0].click();", nested_menu)

    def check_nested_frames(self):
        self.logger.info("Переключаемся на родительский фрейм")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.PARENT_FRAME))
        parent_text = self.wait.until(EC.visibility_of_element_located(self.PARENT_BODY)).text

        self.logger.info("Переключаемся на дочерний фрейм")
        child = self.wait.until(EC.presence_of_element_located(self.CHILD_FRAME))
        self.driver.switch_to.frame(child)
        child_text = self.wait.until(EC.visibility_of_element_located(self.CHILD_PARAGRAPH)).text

        self.driver.switch_to.default_content()
        self.logger.info(f"Текст родительского фрейма: {parent_text}")
        self.logger.info(f"Текст дочернего фрейма: {child_text}")

        return (self.PARENT_TEXT in parent_text) and (self.CHILD_TEXT in child_text)

    def go_to_frames(self):
        self.logger.info("Переходим в меню Frames")
        frames_menu = self.wait.until(EC.presence_of_element_located(self.FRAMES_MENU))
        self.driver.execute_script("arguments[0].click();", frames_menu)

    def check_frames_texts(self):
        self.logger.info("Проверяем текст в Frame1")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME1))
        text1 = self.wait.until(EC.visibility_of_element_located(self.FRAME_HEADING)).text
        self.driver.switch_to.default_content()

        self.logger.info("Проверяем текст в Frame2")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME2))
        text2 = self.wait.until(EC.visibility_of_element_located(self.FRAME_HEADING)).text
        self.driver.switch_to.default_content()

        self.logger.info(f"Текст в Frame1: {text1}, текст в Frame2: {text2}")

        return text1 == text2
