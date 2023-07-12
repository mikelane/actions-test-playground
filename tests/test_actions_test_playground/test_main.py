from __future__ import annotations

from actions_test_playground.main import get_hello


def it_prints_hi_to_the_project_author() -> None:
    expected = 'Hello, Mike lane!'
    actual = get_hello('Mike lane')
    assert actual == expected
