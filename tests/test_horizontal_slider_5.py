from pages.horizontal_slider_page import HorizontalSliderPage


def test_horizontal_slider(driver):
    page = HorizontalSliderPage(driver)
    page.open()
    page.is_opened()
    assert page.set_random_slider_value()
