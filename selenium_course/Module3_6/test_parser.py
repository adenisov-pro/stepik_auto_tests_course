# Путь для запуска:
# pytest -s -v selenium_course/Module3_6/test_parser.py
# pytest -s -v --browser_name=firefox selenium_course/Module3_6/test_parser.py



from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

#pytest -s -v -m "not smoke" test_fixture8.py