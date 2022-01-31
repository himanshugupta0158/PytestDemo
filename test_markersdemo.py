import pytest

# for using markers we need to import pytest.

# this is our custom marker. 
@pytest.mark.smoke
def test_login():
    print("Login Done")


@pytest.mark.regression
def test_addProduct():
    print("Add Products")


@pytest.mark.smoke
def test_logout():
    print("Logout Done")





