import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option('useAutomationExtension', False)
        chromeOptions.add_argument('--disable-extensions')
        driver = webdriver.Chrome(options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities(),
                                  executable_path='C:/Users/cnallan/PycharmProjects/Python_Selenium/drivers/chromedriver.exe')
    elif browser == 'firefox':
        firfoxOptions = webdriver.FirefoxOptions()

        # firfoxOptions.add_experimental_option('useAutomationExtension', False)
        firfoxOptions.add_argument('--disable-extensions')
        driver = webdriver.Chrome(options=firfoxOptions, desired_capabilities=firfoxOptions.to_capabilities(),
                                  executable_path='C:/Users/cnallan/PycharmProjects/Python_Selenium/drivers/geckodriver.exe')

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("TestCompleted")
