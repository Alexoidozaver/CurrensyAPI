from Parser.parser import get_currency
from updater.database_helper import update_db, update_postgres

if __name__ == '__main__':
    currency_course_data = get_currency()
    update_postgres()
    update_db(currency_course_data)


# get_html
# get data
# delete data
# insert data
