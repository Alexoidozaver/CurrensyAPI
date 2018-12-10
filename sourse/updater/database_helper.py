from pymongo import MongoClient


def update_db(currency_course_data):
    client = MongoClient()
    db = client.currency
    posts = db.posts
    posts.delete_many({})
    posts.insert_many(currency_course_data)
