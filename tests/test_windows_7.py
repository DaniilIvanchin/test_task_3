from pages.windows_page import WindowsPage

def test_windows(driver, logger):
    page = WindowsPage(driver, logger)

    page.open()
    page.is_opened()

    page.click_link()
    page.switch_to_tab(1)
    assert page.get_new_window_text() == "New Window"
    assert page.get_tab_title() == "New Window"

    page.switch_to_tab(0)
    page.is_opened()
    page.click_link()
    page.switch_to_tab(2)
    assert page.get_new_window_text() == "New Window"
    assert page.get_tab_title() == "New Window"

    page.switch_to_tab(1)
    page.close_current_tab()
    page.switch_to_tab(1)
    page.close_current_tab()
    page.switch_to_tab(0)
    page.is_opened()