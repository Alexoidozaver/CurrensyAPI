from pymongo import MongoClient
import urllib.request
from constants import currency_url
from Parser.parser import CurrencyParser

if __name__ == '__main__':
    f = urllib.request.urlopen(currency_url)
    parser = CurrencyParser()
    html = f.read()
    html = html.decode("utf-8")
    parser.feed(html)
    currency_course_data = parser.currency_course_data
    client = MongoClient()
    db = client.currency
    collection = db.currency_collection
    posts = db.posts

    posts.delete_many({})
    posts.insert_many(currency_course_data)

# get_html
# get data
# delete data
# insert data
