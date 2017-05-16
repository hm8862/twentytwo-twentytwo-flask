import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail,  Message
from flask.ext.sqlalchemy import SQLAlchemy

import stripe
import jinja2
import datetime
import copy
import uuid


from config import ErrorMessages

#################################################################################
# Define environment

mail = Mail()
app = Flask(__name__, static_folder="static")
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

mail.init_app(app)

stripe_keys = dict(
	secret_key=app.config["STRIPE_SECRET"],
	publishable_key=app.config["STRIPE_PUBLISHABLE"]
)

stripe.api_key = stripe_keys["secret_key"]

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

#################################################################################

import models
import forms
import helpers


#################################################################################
# Display home page
@app.route('/')
def home():
	return render_template("index.html", environment=os.environ['APP_SETTINGS'], cart_item_count=helpers.cart_item_count())

#################################################################################
# Most pages only contain static content, generic method to render static template
@app.route('/<page>')
def staticPage(page):
	return render_template('{}.html'.format(page), environment=os.environ['APP_SETTINGS'], cart_item_count=helpers.cart_item_count())

#################################################################################
### SHOP ###

# Display all shop items in pairs
@app.route('/shop')
def shop():

	# get all shop items and photos
	items = models.ShopItem.query.all()
	photos = models.Photo.query.all()
	item_photos = models.ShopItemPhoto.query.all()

	# map photos to items
	for i in range(0, len(items)):
		item = items[i]

		for item_photo in item_photos:
			if item.id == item_photo.shop_item_id and item_photo.is_thumbnail:
				for photo in photos:
					if photo.id == item_photo.photo_id:
						items[i].image = photo.url

	# split into pairs
	items = zip(*[iter(items)]*2)

	cart_item_count = helpers.cart_item_count()
	print cart_item_count

	return render_template('shop.html', environment=os.environ['APP_SETTINGS'], items=items, cart_item_count=helpers.cart_item_count())

@app.route('/shop/item/<itemId>', methods=["GET", "POST"])
def shopItem(itemId):

	form = forms.ShopItemForm(request.form)

	# get all photos, colours and sizes for mapping
	photos = models.Photo.query.all()
	colours = models.Colour.query.all()
	sizes = models.Size.query.all()

	# get shop item and photos
	item = models.ShopItem.query.filter_by(id=itemId).one()
	thumbnail = models.ShopItemPhoto.query.filter_by(shop_item_id=itemId).filter_by(is_thumbnail=True).one()
	item_photos = models.ShopItemPhoto.query.filter_by(shop_item_id=itemId).all()
	item_colours = models.ShopItemColour.query.filter_by(shop_item_id=itemId).all()
	item_sizes = models.ShopItemSize.query.filter_by(shop_item_id=itemId).all()

	# add colour and size options for given item
	form.size_id.choices = [(size.id, size.name.upper()) for size in models.Size.query.filter(models.Size.id.in_([i.size_id for i in item_sizes])).order_by('id').all()]
	form.colour_id.choices = [(colour.id, colour.name.upper()) for colour in models.Colour.query.filter(models.Colour.id.in_([i.colour_id for i in item_colours])).order_by('name').all()]

	# print dir(form)
	
	if request.method == "POST" and form.validate():

		print "Adding to cart"
		helpers.add_to_cart(itemId)
		return redirect(request.referrer)

	print form.errors


	# # get all photos, colours and sizes for mapping
	# photos = models.Photo.query.all()
	# colours = models.Colour.query.all()
	# sizes = models.Size.query.all()

	# # get shop item and photos
	# item = models.ShopItem.query.filter_by(id=itemId).one()
	# thumbnail = models.ShopItemPhoto.query.filter_by(shop_item_id=itemId).filter_by(is_thumbnail=True).one()
	# item_photos = models.ShopItemPhoto.query.filter_by(shop_item_id=itemId).all()
	# item_colours = models.ShopItemColour.query.filter_by(shop_item_id=itemId).all()
	# item_sizes = models.ShopItemSize.query.filter_by(shop_item_id=itemId).all()

	# # add colour and size options for given item
	# form.size_id.choices = [(-1, "SELECT SIZE")] + [(size.id, size.name.upper()) for size in models.Size.query.filter(models.Size.id.in_([i.size_id for i in item_sizes])).order_by('id').all()]
	# form.colour_id.choices = [(-1, "SELECT SIZE")] + [(colour.id, colour.name.upper()) for colour in models.Colour.query.filter(models.Colour.id.in_([i.colour_id for i in item_colours])).order_by('name').all()]

	# map photo path to item_photos
	for i in range(0, len(item_photos)):
		item_photo = item_photos[i]
		for photo in photos:
			if thumbnail.photo_id == photo.id:
				item.thumbnail = photo.url
			if item_photo.photo_id == photo.id:
				item_photos[i].url = photo.url

	item.images = [item_photo.url for item_photo in item_photos]
	# item.colours = item_colours #[item_colour.name.upper() for item_colour in item_colours]
	# item.sizes = item_sizes #[item_size.name.upper() for item_size in item_sizes]

	errors = session["shop-item-errors"] if "shop-item-errors" in session else None

	return render_template('shop-item.html', environment=os.environ['APP_SETTINGS'], item=item, form=form, cart_item_count=helpers.cart_item_count())

@app.route("/shop/add_to_cart/<int:itemId>", methods=["POST"])
def add_to_cart(itemId):

	itemId = itemId
	size = request.form.get("item-size")
	colour = request.form.get("item-colour")

	# check size and colour have been set
	valid_size = helpers.validate_size(size)
	valid_colour = helpers.validate_colour(colour)
	if not valid_size or not valid_colour:
		
		error_size_message = ErrorMessages.ITEM_SIZE if not valid_size else ""
		error_colour_message = ErrorMessages.ITEM_COLOUR if not valid_colour else ""

		errors = dict(size=error_size_message, colour=error_colour_message)
		session["shop-item-errors"] = errors
		return redirect(url_for("shopItem", itemId=itemId))

	session["shop-item-errors"] = None

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
	return redirect(request.referrer)

@app.route("/shop/cart", methods=["GET", "POST"])
def shop_cart():
 
	if request.method == "GET":
		if "cart" not in session or len(session["cart"]) == 0:
			return render_template("cart.html", environment=os.environ['APP_SETTINGS'], items=[], total=0, cart_item_count=helpers.cart_item_count())

		cart_items, total_amount = helpers.get_cart_items()

		return render_template("cart.html", environment=os.environ['APP_SETTINGS'], cart=cart_items, total=total_amount, cart_item_count=helpers.cart_item_count())

	if request.method == "POST":
		pass

@app.route("/shop/payment-form", methods=["GET", "POST"])
def payment_form():
	form = forms.UserForm(request.form)
	if request.method == "POST" and form.validate():
		print "Validated"
		return redirect(url_for('payment_form'))
	print "Invalid"
	print form.errors
	return render_template('payment-form.html', form=form)

@app.route("/shop/payment", methods=["GET", "POST"])
def pay():

	form = forms.PaymentForm(request.form)

	if request.method == "POST" and form.validate():
		print request.form

		# Get the credit card details submitted by the form
		token = request.form.get('stripeToken')
		email = request.form.get('email')
		billing_first_name = request.form.get('billing_first_name')
		billing_last_name = request.form.get('billing_first_name')
		billing_street = request.form.get('billing_street')
		billing_city = request.form.get('billing_city')
		billing_zip = request.form.get('billing_zip')
		billing_country = request.form.get('billing_country')
		delivery_first_name = request.form.get('delivery_first_name')
		delivery_last_name = request.form.get('delivery_first_name')
		delivery_street = request.form.get('delivery_street')
		delivery_city = request.form.get('delivery_city')
		delivery_zip = request.form.get('delivery_zip')
		delivery_country = request.form.get('delivery_country')
		total = int(float(request.form.get('total')) * 100)
		# total_amount = int(request.form.get('total') * 100.0) # convert to pence

		""" TO DO: get basket details """

		# Create a charge: this will charge the user's card
		try:
			charge = stripe.Charge.create(
				amount=total, # Amount in cents
				currency=app.config['CURRENCY'],
				source=token,
				description=email
			)
		except stripe.error.CardError as e:
			# The card has been declined
			return """<html><body><h1>Card Declined</h1><p>Your chard could not
		be charged. Please check the number and/or contact your credit card
		company.</p></body></html>"""

		print charge

		# clear shopping basket
		session["cart"] = {}

		purchase = models.Purchase(id=str(uuid.uuid4()),
				email=email,
				billing_first_name=billing_first_name,
				billing_last_name=billing_last_name,
				billing_street=billing_street,
				billing_city=billing_city,
				billing_zip=billing_zip,
				billing_country=billing_country,
				delivery_first_name=delivery_first_name,
				delivery_last_name=delivery_last_name,
				delivery_street=delivery_street,
				delivery_city=delivery_city,
				delivery_zip=delivery_zip,
				delivery_country=delivery_country)
		db.session.add(purchase)
		db.session.commit()
		message = Message(
				subject='Thanks for your purchase!',
			sender=app.config["MAIL_USERNAME"], 
			html="""<html><body><h1>Thank you for your purchase of {}!</h1> Your purchase number: {}
			<html><body>""".format(total, purchase.id),
			recipients=[email])
		with mail.connect() as conn:
			conn.send(message)

		return render_template("payment-confirmation.html", environment=os.environ['APP_SETTINGS'], cart_item_count=helpers.cart_item_count())     

	if "cart" not in session.keys():
		return redirect(url_for("shop_cart"))

	items = models.ShopItem.query.all()

	cart_items = []
	total_amount = 0

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
	
	return render_template("payment.html", environment=os.environ['APP_SETTINGS'], 
		key=stripe_keys["publishable_key"],
		shipping=4.95,
		total=total_amount,
		form=form,
		cart_item_count=helpers.cart_item_count()
		)
#################################################################################
### PRESS ###

# Display all press articles, newest first
@app.route('/press')
def press():
	
	# get press articles and photos from database
	articles = models.Press.query.all()
	photos = models.Photo.query.all()
	article_photos = models.PressPhoto.query.all()

	# format date string and append image link to each article
	for i in range(0, len(articles)):
		article = articles[i]
		articles[i].published_str = datetime.datetime.strftime(article.published, "%B %Y").upper()

		for article_photo in article_photos:
			if article.id == article_photo.press_id:
				for photo in photos:
					if photo.id == article_photo.photo_id:
						articles[i].image = photo.url

	# display newest article first
	articles.reverse()

	return render_template('press.html', environment=os.environ['APP_SETTINGS'], articles=articles, cart_item_count=helpers.cart_item_count())


if __name__ == '__main__':
	app.run()