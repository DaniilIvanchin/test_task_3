from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import tempfile
import os


class UploadPage(BasePage):
    URL = "http://the-internet.herokuapp.com/upload"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='File Uploader']")
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    SUCCESS_TEXT = (By.XPATH, "//h3[text()='File Uploaded!']")
    UPLOADED_FILE_NAME = (By.ID, "uploaded-files")

    def is_opened(self):
        self.logger.info("Проверяем, что страница загрузки файлов открыта")
        return self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE_LOCATOR))

    def upload_temp_file(self, content=b"Hello"):
        self.logger.info("Создаем временный файл для загрузки")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        temp_file.write(content)
        temp_file.close()

        try:
            self.logger.info(f"Выбираем файл: {temp_file.name}")
            file_input = self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
            file_input.send_keys(os.path.abspath(temp_file.name))

            self.logger.info("Нажимаем кнопку Upload")
            self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

            self.logger.info("Ждем подтверждения успешной загрузки файла")
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))
            uploaded_name = self.wait.until(EC.visibility_of_element_located(self.UPLOADED_FILE_NAME)).text
            self.logger.info(f"Файл успешно загружен: {uploaded_name}")

            return uploaded_name, os.path.basename(temp_file.name)

        finally:
            os.unlink(temp_file.name)
            self.logger.info(f"Временный файл удален: {temp_file.name}")


class FileUploadPage(BasePage):
    URL = "http://the-internet.herokuapp.com/upload"

    CHECK_PAGE_LOCATOR = (By.XPATH, "//h3[text()='File Uploader']")
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_MESSAGE = (By.XPATH, "//h3[text()='File Uploaded!']")
    UPLOADED_FILE = (By.ID, "uploaded-files")

    TEST_FILE = "Upload_file_test.txt"

    def upload_file(self):
        abs_path = os.path.abspath(self.TEST_FILE)
        self.logger.info(f"Загружаем файл: {abs_path}")
        file_input = self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(abs_path)

        self.logger.info("Нажимаем кнопку Upload")
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_BUTTON)).click()

    def is_uploaded(self):
        self.logger.info("Проверяем, что файл успешно загружен")
        self.wait.until(EC.presence_of_element_located(self.UPLOADED_MESSAGE))
        uploaded_file = self.wait.until(EC.presence_of_element_located(self.UPLOADED_FILE)).text
        self.logger.info(f"Имя загруженного файла: {uploaded_file}")
        return self.TEST_FILE in uploaded_file
