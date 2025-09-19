from pages.javascript_alerts_page import JavaScriptAlertsPage
from pages.javascript_alerts_page import JavaScriptAlertsPageJS

def test_javascript_alerts_page_2(driver):
    page = JavaScriptAlertsPage(driver)
    page.open()
    page.is_opened()
    assert page.click_js_alert()
    assert page.click_js_confirm()
    assert page.click_js_prompt()


def test_javascript_alerts_page_3(driver):
    page = JavaScriptAlertsPageJS(driver)
    page.open()
    page.is_opened()
    assert page.js_alert()
    assert page.js_confirm()
    assert page.js_prompt()