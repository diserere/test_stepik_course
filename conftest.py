import pytest

print()


@pytest.fixture(scope="function", autouse=True)
def delim():
    print()
    yield
    print()
