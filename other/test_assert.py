from assertpy import assert_that, soft_assertions
from icecream import ic


def test_assert():
    ic()
    ic(False)
    assert False is True
    ic(True)
    assert True


def test_soft_assert():
    ic()
    with soft_assertions():  # pyright: ignore[reportGeneralTypeIssues]
        ic(False)
        assert False is True
        ic(True)
        assert True


def test_soft_assertpy():
    ic()
    with soft_assertions():  # pyright: ignore[reportGeneralTypeIssues]
        ic(False)
        assert_that(False).is_true().is_equal_to("qwe")
        ic(False)
        assert_that(False).is_equal_to(True)
        ic(True)
        assert_that(True)
