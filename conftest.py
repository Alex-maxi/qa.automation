import pytest
from src.data.models.users import User


@pytest.fixture(scope="function")
def user():
    #before test
    print("Create user")
    user = User(43)

    #pass user object to test
    yield user

    # after test  
    print("Remove user")
    user.remove()
    