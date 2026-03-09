import pytest
# from icecream import ic


print()


@pytest.fixture(scope="function", autouse=True)
def delim():
    print()
    yield
    print()
    # ic()
