import pytest
from icecream import ic

from utils.utils import safe


class TestUtils:
    @pytest.mark.parametrize("x", [1, 2, 0])
    def test_safe(self, x):
        """Test safe() contextmanager."""
        with safe():
            ic(x)
            ic(12 / x) # pyright: ignore[reportOperatorIssue]
            ic("Aviod division by zero")
