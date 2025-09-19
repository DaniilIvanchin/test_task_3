from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.config_reader import ConfigReader
import logging

class BasePage:
    DEFAULT_TIMEOUT = 10
    CHECK_PAGE_LOCATOR = None
    TEXT_LOCATOR = None
    URL = None

    def __init__(self, driver, logger=None):
        timeout = ConfigReader.get("timeout", self.DEFAULT_TIMEOUT)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

        self.logger = logger or logging.getLogger("default_logger")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def open(self, url=None):

        base_url = url or self.URL
        if not base_url:
            raise ValueError("URL не задан ни в методе, ни в классе")
        self.logger.info(f"Открываем страницу: {base_url}")
        self.driver.get(base_url)

    def is_opened(self):
        self.logger.info(f"Проверка открытия страницы: {self.driver.current_url}")
        self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE_LOCATOR))
