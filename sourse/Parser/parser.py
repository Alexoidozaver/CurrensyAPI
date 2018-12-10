from html.parser import HTMLParser
import urllib.request

from constants import FOUND, NOT_FOUND, currency_url
from Parser.parser_helpers import (
    currency_name,
    currency_name_data,
    main_currency_table,
    currency_field,
    end_of_table,
)


class CurrencyParser(HTMLParser):
    table_status = NOT_FOUND
    new_currency = False
    currency_course_data = []
    iterator = -1

    def handle_starttag(self, tag, attrs):
        if main_currency_table(tag, attrs):
            self.table_status = FOUND
            return

        if currency_field(self.table_status, tag):
            if currency_name(attrs):
                self.new_currency = True
                return
            self.currency_course_data[self.iterator][attrs[1][1]] = attrs[2][1]
            return

        if currency_name_data(self.new_currency, tag):
            start_data_dict = {"name": attrs[2][1]}
            self.currency_course_data.append(start_data_dict)
            self.iterator += 1
            self.new_currency = False
            return

    def handle_endtag(self, tag):
        if end_of_table(self.table_status, tag):
            self.table_status = NOT_FOUND
            return

    def handle_data(self, data):
        pass


def get_currency():
    f = urllib.request.urlopen(currency_url)
    parser = CurrencyParser()
    html = f.read()
    html = html.decode("utf-8")
    parser.feed(html)
    return parser.currency_course_data
