from flask import session
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

import models

def validate_size(size_id):
	try:
		size = models.Size.query.filter_by(id=size_id).one()
	except (MultipleResultsFound, NoResultFound):
		return False
	if size is None:
		return False

	return size_id

def validate_colour(colour_id):
	try:
		colour = models.Colour.query.filter_by(id=colour_id).one()
	except (MultipleResultsFound, NoResultFound):
		return False
	if colour is None:
		return False

	return colour_id

def get_cart_items():

	items = models.ShopItem.query.all()
	sizes = models.Size.query.all()
	colours = models.Colour.query.all()
	photos = models.Photo.query.all()
	item_thumbnails = models.ShopItemPhoto.query.filter_by(is_thumbnail=True).all()

	cart_items = []
	total_amount = 0

	# map item, size and colour meta to items in shopping cart
	for cart_item in session["cart"]:
		cart_item_id, cart_item_size, cart_item_colour = cart_item.split("|")
		cart_item_quantity = session["cart"][cart_item]
		for item in items:
			if int(cart_item_id) == item.id:
				cart_item = dict(id=item.id,
					name=item.name,
					category=item.category,
					quantity=cart_item_quantity,
					price=item.price)
				total_amount += item.price * cart_item_quantity

				for item_thumbnail in item_thumbnails:
					if item_thumbnail.shop_item_id == item.id:
						for photo in photos:
							if item_thumbnail.photo_id == photo.id:
								cart_item["thumbnail"] = photo.url

		for size in sizes:
				if int(cart_item_size) == size.id:
					cart_item["size"] = size

		for colour in colours:
			if int(cart_item_colour) == colour.id:
				cart_item["colour"] = colour

		cart_items.append(cart_item)

	return cart_items, total_amount