import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir),
)

from Parser.parser import get_currency  # noqa


def test_parser():
    currency_course_data = get_currency()
    assert len(currency_course_data) == 14
