from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Float, nullable=False)


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)
    farm = db.relationship('Farm', backref='weather')


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)
    farm = db.relationship('Farm', backref='equipment')
