import pytest
import sys 


@pytest.mark.parametrize("username,password",
                         [
                             ("Selenium","WebDriver"),
                             ("Python","Pytest"),
                             ("Java","Swing"),
                             ("API","Web Automachine")
                         ])
def test_login(username,password):
    print(username)
    print(password)