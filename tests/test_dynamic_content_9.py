from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content_page(driver):
    page = DynamicContentPage(driver)
    page.open()
    page.is_opened()

    assert page.reload_until_match()