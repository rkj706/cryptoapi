from mongoengine import Document, EmbeddedDocument, fields


class CoinList(Document):
    coin_name = fields.StringField(required=True, max_length=200)
    usd_price = fields.FloatField(required=True)
    usd_market_cap = fields.FloatField(required=True)
    usd_24Hr_vol = fields.FloatField(required=True)
    usd_24h_change = fields.DecimalField(precision=2)
    last_updated_at = fields.DateTimeField()


class CoinGraph(Document):
    coin_name = fields.StringField(required=True, max_length=200)
    hourly_data = fields.ListField()
    twelve_hr_data = fields.ListField()
    daily_data = fields.ListField()
    weekly_data = fields.ListField()
    monthly_data = fields.ListField()
    yearly_data = fields.ListField()