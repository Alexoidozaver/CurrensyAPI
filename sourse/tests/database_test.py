import sys
import os
from pymongo import MongoClient

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir),
)
from constants import TEST_CURRENCY  # noqa
from updater.database_helper import update_db  # noqa


def updater_test():
    update_db(TEST_CURRENCY)
    client = MongoClient()
    db = client.currency
    posts = db.posts
    post_list = []

    for post in posts.find():
        post_list.append(post)

    assert post_list == TEST_CURRENCY
