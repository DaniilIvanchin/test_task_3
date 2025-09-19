import pytest
from core.browser import Browser
from core.config_reader import ConfigReader
import logging
import os

@pytest.fixture
def driver():
    config = ConfigReader.load_config()
    browser_cfg = config["browser"]

    browser = Browser(options_list=browser_cfg.get("options", []))
    yield browser.driver
    browser.quit()

@pytest.fixture(scope="session")
def logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "tests.log")

    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    return logger


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        logger = item.funcargs.get("logger", None)

        if driver:
            screenshot_dir = os.path.join("logs", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(file_name)

            if logger:
                logger.error(f"Тест фоллс: {item.name}, скриншот сохранён: {file_name}")