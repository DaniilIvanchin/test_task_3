from pages.demoqa_frames_page import FramesPage


def test_frames_and_nested_frames(driver):
    page = FramesPage(driver)
    page.open()
    page.is_opened()
    page.ensure_menu_open()
    page.go_to_nested_frames()
    assert page.check_nested_frames()

    page.go_to_frames()
    assert page.check_frames_texts()
