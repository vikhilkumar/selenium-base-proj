#Session 48

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")   #use of this is.. to call this setup function inside test_searchflights class. scope='class' will applicable class level.
def setup(request):           #request fixture is a special fixture providing  information of the requesting test function.
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver,10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.wait = wait
    yield              #Anything you put after yield is teardown method
    driver.close()