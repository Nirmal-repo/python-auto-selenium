import pytest
from selenium import webdriver
@pytest.fixture(scope='class')
def setUp(request):
    baseUrl = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    request.cls.driver = driver
    yield
    driver.quit()