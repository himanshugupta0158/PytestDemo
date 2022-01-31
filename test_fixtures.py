from lib2to3.pgen2 import driver
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
FIXTURES : 

precondtions :
Setup , Connection , API
ready data then, run Test.

Assertion,

Postcondition:
clean,close

fixtures as test is being broken down into 4 steps :
1.> Arrange
2.> Act
3.> Assert
4.> Cleanup

"""
driver = None

@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")


def test_1(setup):
    driver.get("http://www.facebook.com")
    print("Test 1 executed.")

def test_2(setup):
    driver.get("http://www.google.com")
    print("Test 2 executed.")
    
def test_3(setup):
    driver.get("http://www.gmail.com")
    print("Test 3 executed.")




