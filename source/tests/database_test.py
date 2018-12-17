import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir),
)

from app import application as app  # noqa
from constants import TEST_CURRENCY  # noqa
from updater.database_helper import update_db  # noqa


def test_updater():
    update_db(TEST_CURRENCY)
    posts = app.posts
    post_list = []

    for post in posts.find():
        post_list.append(post)

    assert post_list == TEST_CURRENCY
