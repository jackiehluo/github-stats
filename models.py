from datetime import datetime
from github-stats import db

class User(db.DynamicDocument):
    id = db.IntField(required=True)
    username = db.StringField(max_length=39, required=True)
    contributions = db.IntField(required=True)
    longest_streak = db.IntField(required=True)
    current_streak = db.IntField(required=True)
    cheater = db.BooleanField(default=False, required=True)
    last_updated = db.DateTimeField(default=datetime.now, required=True)