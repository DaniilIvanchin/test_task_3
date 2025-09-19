from pages.basic_auth_page import BasicAuthPage

def test_basic_auth(driver, logger):
    page = BasicAuthPage(driver)
    page.open_with_auth()
    page.get_message()
    assert page.get_page_text()
