from currency.currency_helper import CurrencyHelper


def registration_api(app):
    app.add_url_rule(
        "/api/currency",
        defaults={"date": None},
        view_func=CurrencyHelper.as_view("health_check"),
        methods=["GET"],
    )
