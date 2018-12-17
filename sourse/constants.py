FOUND = "found"
NOT_FOUND = "not found"
TABLE = "table"
CURRENCY_URL = "https://kurs.com.ua/"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost" \
                          ":5432/postgres"

TEST_CURRENCY = [
    {
        "name": "Доллар",
        "bid": "27.716667",
        "bid_change": "-0.016",
        "ask": "28.039167",
        "ask_change": "-0.007501",
        "commercial": "27.966",
        "commercial_change": "-0.047",
        "centralbank": "27.824246",
        "centralbank_change": "-0.055323",
    },
    {
        "name": "Евро",
        "bid": "31.435833",
        "bid_change": "0.096",
        "ask": "32.084167",
        "ask_change": "0.129",
        "commercial": "31.923748",
        "commercial_change": "0.005456",
        "centralbank": "31.63895",
        "centralbank_change": "-0.007149",
    },
    {
        "name": "Рубль",
        "bid": "0.368",
        "bid_change": "0.0034",
        "ask": "0.429727",
        "ask_change": "0.004",
        "commercial": "0.421365",
        "commercial_change": "-0.000254",
        "centralbank": "0.41577",
        "centralbank_change": "-0.00198",
    },
]

# postgres settings
PASSWORD = "postgres"
USER = "postgres"
PASSWORD = "postgres"
