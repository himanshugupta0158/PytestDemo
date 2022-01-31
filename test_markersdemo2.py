import pytest
import sys 

# for using markers we need to import pytest.

# this is pre-defined marker.

# below will be skipped from execution/run . 
@pytest.mark.skip
def test_login():
    print("Login Done")

# providing condition for skip if condition satisfies.
@pytest.mark.skipif(sys.version_info<(3,9) , reason="Python version not supported")
def test_addProduct():
    print("Add Products")

# we are expecting below test to be failed.
@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout Done")

@pytest.mark.parametrize
def test_closeApplication():
    assert True
    print("Close the application.")




