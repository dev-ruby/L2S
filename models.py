from app import db


class Uri(db.Model):
    shorted_url = db.Column(db.String(20), primary_key=True)
    target_url = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
