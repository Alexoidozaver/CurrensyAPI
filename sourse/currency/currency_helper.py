from flask.views import MethodView
from flask import jsonify


class CurrencyHelper(MethodView):
    def get(self):
        from updater.database_helper import get_currency_from_db
        currency = get_currency_from_db()
        return jsonify(currency)
