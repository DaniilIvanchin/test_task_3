from pages.hovers_page import HoversPage


def test_hovers_page(driver):
    page = HoversPage(driver)
    page.open()
    page.is_opened()

    user_count = page.get_user_count()
    for i in range(user_count):
        assert page.hover_user_and_open_profile(i)
