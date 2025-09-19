from pages.upload_page import UploadPage
from pages.upload_page import FileUploadPage

def test_upload_11(driver):
    page = UploadPage(driver)
    page.open()
    page.is_opened()

    uploaded_name, expected_name = page.upload_temp_file()
    assert uploaded_name == expected_name

def test_file_upload_12(driver):
    page = FileUploadPage(driver)
    page.open()
    page.is_opened()

    page.upload_file()
    assert page.is_uploaded()



