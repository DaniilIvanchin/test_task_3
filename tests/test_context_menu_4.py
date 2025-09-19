from pages.context_menu_page import ContextMenuPage


def test_context_menu(driver):
    page = ContextMenuPage(driver)
    page.open()
    page.is_opened()
    assert page.trigger_context_menu()
