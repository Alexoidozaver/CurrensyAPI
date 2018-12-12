import pandas as pd
import datetime
from app import application as app
from currency.currency_model import Currency


def update_db(currency_course_data):
    app.posts.delete_many({})
    app.posts.insert_many(currency_course_data)


def get_currency_from_db():
    posts = app.posts.find()
    post_list = []
    for post in posts:
        post["_id"] = str(post["_id"])
        post_list.append(post)
    return post_list


def update_postgress():
    currency = get_currency_from_db()
    currense_data_frame = pd.DataFrame.from_records(currency)
    currense_data_frame["data"] = [datetime.datetime.now().date() for i in
                                   range(len(currency))
                                   ]
    currense_data_frame.to_sql(
        "currency",
        app.sqlalchemy,
        if_exists='append'
    )


def get_currency_from_postgress():
    data = app.session.query(Currency).all()
    conn = app.sqlalchemy.connect()
    cursor = conn.connection.cursor()
    cursor.execute("SELECT * FROM currensy WHERE 1")
    return data
