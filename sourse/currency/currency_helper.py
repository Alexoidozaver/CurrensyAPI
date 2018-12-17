from flask.views import MethodView
from flask import jsonify


class CurrencyHelper(MethodView):
    @staticmethod
    def get(date):
        if date is None:
            from updater.database_helper import get_currency_from_db
            currency = get_currency_from_db()
            return jsonify(currency)
        from updater.database_helper import get_currency_by_date
        currency = get_currency_by_date(date)
        return jsonify(currency)
