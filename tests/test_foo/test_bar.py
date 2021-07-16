import pytest

from foo.bar import add_two


@pytest.mark.parametrize("first, second, expected", [(0, 0, 0), (-1, 2, 1)])
def test_add_two(first, second, expected):
    """Test if :py:func:`add_two` behaves correctly."""
    assert add_two(first, second) == expected
