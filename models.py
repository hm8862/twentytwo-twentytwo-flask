from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey
from datetime import datetime

##########################################################################################
# General models

class Photo(db.Model):
    __tablename__ = 'photo'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String()) # CDN URL once set up

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)

##########################################################################################
# Shop models

class Colour(db.Model):
    __tablename__ = 'colour'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Size(db.Model):
    __tablename__ = 'size'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class ShopItem(db.Model):
    __tablename__ = 'shop_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Numeric(19,2))
    currency = db.Column(db.String(3))
    dna = db.Column(db.String())
    care = db.Column(db.String())

    def __init__(self, name, category, description, price, dna, care, currency="GBP"):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.currency = currency
        self.dna = dna
        self.care = care

    def __repr__(self):
        return '<id {}>'.format(self.id)

class ShopItemColour(db.Model):
    __tablename__ = 'shop_item_colour'

    id = db.Column(db.Integer, primary_key=True)
    shop_item_id = db.Column(ForeignKey("shop_item.id"), nullable=False)
    colour_id = db.Column(ForeignKey("colour.id"), nullable=False)

    def __init__(self, shop_item_id, colour_id):
        self.shop_item_id = shop_item_id
        self.colour_id = colour_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

class ShopItemSize(db.Model):
    __tablename__ = 'shop_item_size'

    id = db.Column(db.Integer, primary_key=True)
    shop_item_id = db.Column(ForeignKey("shop_item.id"), nullable=False)
    size_id = db.Column(ForeignKey("size.id"), nullable=False)

    def __init__(self, shop_item_id, size_id):
        self.shop_item_id = shop_item_id
        self.size_id = size_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

class ShopItemPhoto(db.Model):
    __tablename__ = 'shop_item_photo'

    id = db.Column(db.Integer, primary_key=True)
    shop_item_id = db.Column(ForeignKey("shop_item.id"), nullable=False)#db.relationship("Press", foreign_keys="Press.id")
    photo_id = db.Column(ForeignKey("photo.id"), nullable=False)
    is_thumbnail = db.Column(db.Boolean, nullable=True)

    def __init__(self, shop_item_id, photo_id, is_thumbnail=False):
        self.shop_item_id = shop_item_id
        self.photo_id = photo_id
        if is_thumbnail:
            self.is_thumbnail = is_thumbnail

    def __repr__(self):
        return '<id {}>'.format(self.id)


##########################################################################################

class Press(db.Model):
    __tablename__ = 'press'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    tag_line = db.Column(db.String())
    link = db.Column(db.String())
    published = db.Column(db.DateTime)

    def __init__(self, title, tag_line, link, published=None):
        self.title = title
        self.tag_line = tag_line
        self.link = link
        if published is None:
            published = datetime.utcnow()
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)

class PressPhoto(db.Model):
    __tablename__ = 'press_photos'

    id = db.Column(db.Integer, primary_key=True)
    press_id = db.Column(ForeignKey("press.id"), nullable=False)#db.relationship("Press", foreign_keys="Press.id")
    photo_id = db.Column(ForeignKey("photo.id"), nullable=False)

    def __init__(self, press_id, photo_id):
        self.press_id = press_id
        self.photo_id = photo_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

##########################################################################################

class Purchase(db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    billing_first_name = db.Column(db.String)
    billing_last_name = db.Column(db.String)
    billing_street = db.Column(db.String)
    billing_city = db.Column(db.String)
    billing_zip = db.Column(db.String)
    billing_country = db.Column(db.String)
    delivery_first_name = db.Column(db.String)
    delivery_last_name = db.Column(db.String)
    delivery_street = db.Column(db.String)
    delivery_city = db.Column(db.String)
    delivery_zip = db.Column(db.String)
    delivery_country = db.Column(db.String)

    def __init__(self, id, email, billing_first_name, billing_last_name, billing_street, billing_city, billing_zip, billing_country,
                delivery_first_name, delivery_last_name, delivery_street, delivery_city, delivery_zip, delivery_country):
        self.id = id 
        self.email = email
        self.billing_first_name = billing_first_name
        self.billing_last_name = billing_last_name 
        self.billing_street = billing_street
        self.billing_city = billing_city
        self.billing_zip = billing_zip
        self.billing_country = billing_country
        self.delivery_first_name = delivery_first_name
        self.delivery_last_name = delivery_last_name
        self.delivery_street = delivery_street
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.delivery_country = delivery_country

    def __repr__(self):
        return '<id {}>'.format(self.id)
