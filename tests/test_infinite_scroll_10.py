from pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll(driver):
    page = InfiniteScrollPage(driver)
    page.open()
    page.is_opened()

    assert page.ensure_paragraphs_loaded()