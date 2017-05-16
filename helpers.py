from flask import session, request
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

def add_to_cart(itemId):

	itemId = itemId
	size = request.form.get("size_id")
	colour = request.form.get("colour_id")

	# # check size and colour have been set
	# valid_size = helpers.validate_size(size)
	# valid_colour = helpers.validate_colour(colour)
	# if not valid_size or not valid_colour:
		
	# 	error_size_message = ErrorMessages.ITEM_SIZE if not valid_size else ""
	# 	error_colour_message = ErrorMessages.ITEM_COLOUR if not valid_colour else ""

	# 	errors = dict(size=error_size_message, colour=error_colour_message)
	# 	session["shop-item-errors"] = errors
	# 	return redirect(url_for("shopItem", itemId=itemId))

	# session["shop-item-errors"] = None

	# create key for item / size / colour combo
	key = "{item_id}|{size_id}|{colour_id}".format(item_id=itemId, size_id=size, colour_id=colour)

	if "cart" not in session:
		# user currently has no shopping cart, initialise
		session["cart"] = {}

	# if item / size / colour combo already exists, increment, else initialise
	if key in session["cart"]:
		session["cart"][key] += 1
	else:
		session["cart"][key] = 1
		
	""" TODO: increment number of items in task bar. """
	print session["cart"]
	return

def cart_item_count():

	if "cart" in session:
		return len(session["cart"])
	return 0

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
			if cart_item_id and int(cart_item_id) == item.id:
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
			if cart_item_size != "None" and int(cart_item_size) == size.id:
				cart_item["size"] = size

		for colour in colours:
			if cart_item_colour != "None" and int(cart_item_colour) == colour.id:
				cart_item["colour"] = colour

		cart_items.append(cart_item)

	return cart_items, total_amount