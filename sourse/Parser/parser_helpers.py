from constants import FOUND, TABLE


def currency_name(attrs):
    return ('class', 'ipsKursTable_currency ipsType_center') in attrs


def currency_name_data(new_currency, tag):
    return new_currency and tag == "a"


def main_currency_table(tag, attrs):
    return tag == TABLE and ('data-role', 'board') in attrs


def currency_field(table_status, tag):
    return table_status == FOUND and tag == "td"


def end_of_table(table_status, tag):
    return table_status == FOUND and tag == TABLE
