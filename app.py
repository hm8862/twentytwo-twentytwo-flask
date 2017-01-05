import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

import jinja2
import datetime

#################################################################################
# Define environment

app = Flask(__name__, static_folder="static")
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

#################################################################################

import models

#################################################################################
# Display home page
@app.route('/')
def home():
    return render_template("index.html", environment=os.environ['APP_SETTINGS'])

#################################################################################
# Most pages only contain static content, generic method to render static template
@app.route('/<page>')
def staticPage(page):
    return render_template('{}.html'.format(page), environment=os.environ['APP_SETTINGS'])

#################################################################################
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

	return render_template('shop.html', environment=os.environ['APP_SETTINGS'], items=items)

@app.route('/shop/item/<itemId>')
def shopItem(itemId):

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

	# map photo path to item_photos
	for i in range(0, len(item_photos)):
		item_photo = item_photos[i]
		for photo in photos:
			if thumbnail.photo_id == photo.id:
				item.thumbnail = photo.url
			if item_photo.photo_id == photo.id:
				item_photos[i].url = photo.url


	# map colour name to item_colours
	for j in range(0, len(item_colours)):
		item_colour = item_colours[j]
		for colour in colours:
			if item_colour.colour_id == colour.id:
				item_colours[j].name = colour.name

	# map size name to item_sizes
	for k in range(0, len(item_sizes)):
		item_size = item_sizes[k]
		for size in sizes:
			if item_size.size_id == size.id:
				item_sizes[k].name = size.name

	# build item meta
	item.images = [item_photo.url for item_photo in item_photos]
	item.colours = [item_colour.name.upper() for item_colour in item_colours]
	item.sizes = [item_size.name.upper() for item_size in item_sizes]

	return render_template('shop-item.html', environment=os.environ['APP_SETTINGS'], item=item)

#################################################################################
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

	return render_template('press.html', environment=os.environ['APP_SETTINGS'], articles=articles)


if __name__ == '__main__':
    app.run()