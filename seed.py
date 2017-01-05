from app import db
from models import Photo, Press, PressPhoto, Colour, Size, ShopItem, ShopItemColour, ShopItemSize, ShopItemPhoto
from datetime import datetime

###############################################################################################################################################################################

def seed_db():
	# Insert Photos

	photo0 = Photo(
		url="ANABEL1.jpeg"
		)
	db.session.add(photo0)
	db.session.commit()

	photo1 = Photo(
		url="ANABEL2.jpeg"
		)
	db.session.add(photo1)
	db.session.commit()

	photo2 = Photo(
		url="ANABEL3.jpeg"
		)
	db.session.add(photo2)
	db.session.commit()

	photo3 = Photo(
		url="EMINNUDE1.jpeg"
		)
	db.session.add(photo3)
	db.session.commit()

	photo4 = Photo(
		url="EMINNUDE2.jpeg"
		)
	db.session.add(photo4)
	db.session.commit()

	photo5 = Photo(
		url="EMINNUDE3.jpg"
		)
	db.session.add(photo5)
	db.session.commit()

	photo6 = Photo(
		url="EMINNUDE4.jpeg"
		)
	db.session.add(photo6)
	db.session.commit()

	photo7 = Photo(
		url="EMINSORBET1.jpeg"
		)
	db.session.add(photo7)
	db.session.commit()

	photo8 = Photo(
		url="EMINSORBET2.jpeg"
		)
	db.session.add(photo8)
	db.session.commit()

	photo9 = Photo(
		url="EMINSORBET3.jpeg"
		)
	db.session.add(photo9)
	db.session.commit()

	photo10 = Photo(
		url="EMINSORBET4.jpeg"
		)
	db.session.add(photo10)
	db.session.commit()

	photo11 = Photo(
		url="GEMMA1.jpeg"
		)
	db.session.add(photo11)
	db.session.commit()

	photo12 = Photo(
		url="GEMMA2.jpeg"
		)
	db.session.add(photo12)
	db.session.commit()

	photo13 = Photo(
		url="GEMMA3.jpeg"
		)
	db.session.add(photo13)
	db.session.commit()

	photo14 = Photo(
		url="GEMMA4.jpeg"
		)
	db.session.add(photo14)
	db.session.commit()

	photo16 = Photo(
		url="JULIA1.jpeg"
		)
	db.session.add(photo16)
	db.session.commit()

	photo17 = Photo(
		url="JULIA2.jpeg"
		)
	db.session.add(photo17)
	db.session.commit()

	photo18 = Photo(
		url="JULIA3.jpeg"
		)
	db.session.add(photo18)
	db.session.commit()

	photo19 = Photo(
		url="JULIA4.jpg"
		)
	db.session.add(photo19)
	db.session.commit()

	photo20 = Photo(
		url="MALLORY1.jpeg"
		)
	db.session.add(photo20)
	db.session.commit()

	photo21 = Photo(
		url="MALLORY2.jpeg"
		)
	db.session.add(photo21)
	db.session.commit()

	photo22 = Photo(
		url="MALLORY3.jpeg"
		)
	db.session.add(photo22)
	db.session.commit()

	photo23 = Photo(
		url="RITAWOOL1.jpeg"
		)
	db.session.add(photo23)
	db.session.commit()

	photo24 = Photo(
		url="RITAWOOL2.jpeg"
		)
	db.session.add(photo24)
	db.session.commit()

	photo25 = Photo(
		url="RITAWOOL3.jpg"
		)
	db.session.add(photo25)
	db.session.commit()

	photo26 = Photo(
		url="VOGUE_IT_PRESS.png"
		)
	db.session.add(photo26)
	db.session.commit()

	# photo1 = PressPhoto(
	# 	article_id=press1.id,
	# 	url="JULIA1.jpeg"
	# 	)
	# db.session.add(photo1)
	# db.session.commit()

	# photo2 = PressPhoto(
	# 	article_id=press2.id,
	# 	url="EMINNUDE1.jpeg"
	# 	)

	# db.session.add(photo2)
	# db.session.commit()

	# photo3 = PressPhoto(
	# 	article_id=press3.id,
	# 	url="VOGUE_IT_PRESS.png"
	# 	)

	# db.session.add(photo3)
	# db.session.commit()

	###############################################################################################################################################################################

	# Insert colours

	colour1 = Colour(name="light pink")
	db.session.add(colour1)
	db.session.commit()

	colour2 = Colour(name="candy")
	db.session.add(colour2)
	db.session.commit()

	colour3 = Colour(name="sorbet")
	db.session.add(colour3)
	db.session.commit()

	colour4 = Colour(name="charcoal blue")
	db.session.add(colour4)
	db.session.commit()

	colour5 = Colour(name="yellow")
	db.session.add(colour5)
	db.session.commit()

	colour6 = Colour(name="oatmeal")
	db.session.add(colour6)
	db.session.commit()

	colour7 = Colour(name="nude")
	db.session.add(colour7)
	db.session.commit()

	colour8 = Colour(name="midnight blue")
	db.session.add(colour8)
	db.session.commit()

	colour9 = Colour(name="white")
	db.session.add(colour9)
	db.session.commit()

	###############################################################################################################################################################################

	# Insert Sizes

	size1 = Size(name="small")
	db.session.add(size1)
	db.session.commit()

	size2 = Size(name="medium")
	db.session.add(size2)
	db.session.commit()

	size3 = Size(name="one-size")
	db.session.add(size3)
	db.session.commit()

	###############################################################################################################################################################################

	# Insert Items

	item3 = ShopItem(
		name="gemma",
		category="trousers",
		description="Sheer silk wide-leg trousers.",
		price=52.00,
		dna="100% Silk",
		care="""Hand-wash only with delicates solution in lukewarm water. Rinse with cold water.
		<br>
		<br>
		<br>
		<br>
		<br>
		<div class="col-md-10">
			<span>HERE, MARION IS WEARING GEMMA IN CANDY</span>
		</div>
		<br>"""
		)
	db.session.add(item3)
	db.session.commit()

	item6 = ShopItem(
		name="emin",
		category="shirt",
		description="Sheer silk capped-sleeve blouse with lapel detail.",
		price=50.00,
		dna="100% Silk",
		care="Hand-wash only with delicates solution in lukewarm water. Rinse with cold water."
		)
	db.session.add(item6)
	db.session.commit()

	item5 = ShopItem(
		name="rita",
		category="top",
		description="Kimono sleeve pullover in washed linen/speckled wool with ruffle detail and yellow trim.",
		price=90.00,
		dna="100% Linen / 100% Wool",
		care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water. Lay flat to dry."
		)
	db.session.add(item5)
	db.session.commit()

	item2 = ShopItem(
		name="julia",
		category="dress",
		description="Light pink, floor-length silk dress with candy pink trim.",
		price=220.00,
		dna="100% Silk",
		care="Hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees."
		)
	db.session.add(item2)
	db.session.commit()

	item8 = ShopItem(
		name="mallory",
		category="dress",
		description="Straight-cut, sleevless dress with low v-neck and back in pressed blue wool. Can also be worn as a tunic.",
		price=110.00,
		dna="100% Wool",
		care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees. Dry flat to retain shape."
		)
	db.session.add(item8)
	db.session.commit()

	item1 = ShopItem(
		name="anabel",
		category="top",
		description="Light pink silk top with yellow trim and floaty hem.",
		price=190.00,
		dna="100% Silk",
		care="Hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees. Dry flat to retain shape."
		)
	db.session.add(item1)
	db.session.commit()

	# item4 = ShopItem(
	# 	name="lydia dress",
	# 	description="Spaghetti-strap slip dress in stonewashed silk.",
	# 	dna="100% Silk",
	# 	care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water."
	# 	)
	# db.session.add(item4)
	# db.session.commit()

	# item7 = ShopItem(
	# 	name="janet jacket",
	# 	description="Straight-cut jacket with exaggerated collar in pressed blue wool.",
	# 	dna="100% Wool",
	# 	care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees. Dry flat to retain shape."
	# 	)
	# db.session.add(item7)
	# db.session.commit()

	# item9 = ShopItem(
	# 	name="lucy shirt",
	# 	description="Flared-sleeve cotton shirt.",
	# 	dna="100% Cotton",
	# 	care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees."
	# 	)
	# db.session.add(item9)
	# db.session.commit()

	# item10 = ShopItem(
	# 	name="audrey trousers",
	# 	description="Cropped, flared trousers in pressed blue wool.",
	# 	dna="100% Wool",
	# 	care="For best results hand-wash with delicates solution in lukewarm water and rinse with cold water. Alternatively, short wash on 30 degrees. Dry flat to retain shape."
	# 	)
	# db.session.add(item10)
	# db.session.commit()

	###############################################################################################################################################################################

	# Create shop item -> colour map

	itemColour1 = ShopItemColour(
		shop_item_id=item1.id,
		colour_id=colour1.id)
	db.session.add(itemColour1)
	db.session.commit()

	itemColour2 = ShopItemColour(
		shop_item_id=item2.id,
		colour_id=colour1.id)
	db.session.add(itemColour2)
	db.session.commit()

	itemColour3 = ShopItemColour(
		shop_item_id=item3.id,
		colour_id=colour2.id)
	db.session.add(itemColour3)
	db.session.commit()

	itemColour4 = ShopItemColour(
		shop_item_id=item3.id,
		colour_id=colour3.id)
	db.session.add(itemColour4)
	db.session.commit()

	# itemColour5 = ShopItemColour(
	# 	shop_item_id=item4.id,
	# 	colour_id=colour4.id)
	# db.session.add(itemColour5)
	# db.session.commit()

	itemColour6 = ShopItemColour(
		shop_item_id=item5.id,
		colour_id=colour5.id)
	db.session.add(itemColour6)
	db.session.commit()

	itemColour7 = ShopItemColour(
		shop_item_id=item5.id,
		colour_id=colour6.id)
	db.session.add(itemColour7)
	db.session.commit()

	itemColour8 = ShopItemColour(
		shop_item_id=item6.id,
		colour_id=colour2.id)
	db.session.add(itemColour8)
	db.session.commit()

	itemColour9 = ShopItemColour(
		shop_item_id=item6.id,
		colour_id=colour3.id)
	db.session.add(itemColour9)
	db.session.commit()

	itemColour10 = ShopItemColour(
		shop_item_id=item6.id,
		colour_id=colour7.id)
	db.session.add(itemColour10)
	db.session.commit()

	# itemColour11 = ShopItemColour(
	# 	shop_item_id=item7.id,
	# 	colour_id=colour8.id)
	# db.session.add(itemColour11)
	# db.session.commit()

	itemColour12 = ShopItemColour(
		shop_item_id=item8.id,
		colour_id=colour8.id)
	db.session.add(itemColour12)
	db.session.commit()

	# itemColour13 = ShopItemColour(
	# 	shop_item_id=item9.id,
	# 	colour_id=colour9.id)
	# db.session.add(itemColour13)
	# db.session.commit()

	# itemColour14 = ShopItemColour(
	# 	shop_item_id=item10.id,
	# 	colour_id=colour8.id)
	# db.session.add(itemColour14)
	# db.session.commit()

	###############################################################################################################################################################################

	# Create shop item -> size map

	itemSize1 = ShopItemSize(
		shop_item_id=item1.id,
		size_id=size1.id)
	db.session.add(itemSize1)
	db.session.commit()

	itemSize2 = ShopItemSize(
		shop_item_id=item1.id,
		size_id=size2.id)
	db.session.add(itemSize2)
	db.session.commit()

	itemSize3 = ShopItemSize(
		shop_item_id=item2.id,
		size_id=size1.id)
	db.session.add(itemSize3)
	db.session.commit()

	itemSize4 = ShopItemSize(
		shop_item_id=item2.id,
		size_id=size2.id)
	db.session.add(itemSize4)
	db.session.commit()

	itemSize5 = ShopItemSize(
		shop_item_id=item3.id,
		size_id=size1.id)
	db.session.add(itemSize5)
	db.session.commit()

	itemSize6 = ShopItemSize(
		shop_item_id=item3.id,
		size_id=size2.id)
	db.session.add(itemSize6)
	db.session.commit()

	# itemSize7 = ShopItemSize(
	# 	shop_item_id=item4.id,
	# 	size_id=size1.id)
	# db.session.add(itemSize7)
	# db.session.commit()

	# itemSize8 = ShopItemSize(
	# 	shop_item_id=item4.id,
	# 	size_id=size2.id)
	# db.session.add(itemSize8)
	# db.session.commit()

	itemSize9 = ShopItemSize(
		shop_item_id=item5.id,
		size_id=size3.id)
	db.session.add(itemSize9)
	db.session.commit()

	itemSize10 = ShopItemSize(
		shop_item_id=item6.id,
		size_id=size3.id)
	db.session.add(itemSize10)
	db.session.commit()

	# itemSize11 = ShopItemSize(
	# 	shop_item_id=item7.id,
	# 	size_id=size3.id)
	# db.session.add(itemSize11)
	# db.session.commit()

	itemSize12 = ShopItemSize(
		shop_item_id=item8.id,
		size_id=size1.id)
	db.session.add(itemSize12)
	db.session.commit()

	itemSize13 = ShopItemSize(
		shop_item_id=item8.id,
		size_id=size2.id)
	db.session.add(itemSize13)
	db.session.commit()

	# itemSize14 = ShopItemSize(
	# 	shop_item_id=item9.id,
	# 	size_id=size1.id)
	# db.session.add(itemSize14)
	# db.session.commit()

	# itemSize15 = ShopItemSize(
	# 	shop_item_id=item9.id,
	# 	size_id=size2.id)
	# db.session.add(itemSize15)
	# db.session.commit()

	# itemSize16 = ShopItemSize(
	# 	shop_item_id=item10.id,
	# 	size_id=size1.id)
	# db.session.add(itemSize16)
	# db.session.commit()

	# itemSize17 = ShopItemSize(
	# 	shop_item_id=item10.id,
	# 	size_id=size2.id)
	# db.session.add(itemSize17)
	# db.session.commit()

	###############################################################################################################################################################################

	# Insert Item Photos

	# "itemPhoto{} = ShopItemPhoto(\n\tshop_item_id={},\n\tphoto_id={}\n\t)\ndb.session.add(itemPhoto{})\ndb.session.commot()\n".format(count, i[0], i[1], count)

	itemPhoto0 = ShopItemPhoto(
		shop_item_id=item1.id,
		photo_id=photo0.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto0)
	db.session.commit()

	itemPhoto1 = ShopItemPhoto(
		shop_item_id=item1.id,
		photo_id=photo1.id
		)
	db.session.add(itemPhoto1)
	db.session.commit()

	itemPhoto2 = ShopItemPhoto(
		shop_item_id=item1.id,
		photo_id=photo2.id
		)
	db.session.add(itemPhoto2)
	db.session.commit()

	itemPhoto3 = ShopItemPhoto(
		shop_item_id=item2.id,
		photo_id=photo16.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto3)
	db.session.commit()

	itemPhoto4 = ShopItemPhoto(
		shop_item_id=item2.id,
		photo_id=photo17.id
		)
	db.session.add(itemPhoto4)
	db.session.commit()

	itemPhoto5 = ShopItemPhoto(
		shop_item_id=item2.id,
		photo_id=photo18.id
		)
	db.session.add(itemPhoto5)
	db.session.commit()

	itemPhoto6 = ShopItemPhoto(
		shop_item_id=item2.id,
		photo_id=photo19.id
		)
	db.session.add(itemPhoto6)
	db.session.commit()

	itemPhoto7 = ShopItemPhoto(
		shop_item_id=item3.id,
		photo_id=photo11.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto7)
	db.session.commit()

	itemPhoto8 = ShopItemPhoto(
		shop_item_id=item3.id,
		photo_id=photo12.id
		)
	db.session.add(itemPhoto8)
	db.session.commit()

	itemPhoto9 = ShopItemPhoto(
		shop_item_id=item3.id,
		photo_id=photo13.id
		)
	db.session.add(itemPhoto9)
	db.session.commit()

	itemPhoto10 = ShopItemPhoto(
		shop_item_id=item3.id,
		photo_id=photo14.id
		)
	db.session.add(itemPhoto10)
	db.session.commit()

	itemPhoto12 = ShopItemPhoto(
		shop_item_id=item5.id,
		photo_id=photo23.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto12)
	db.session.commit()

	itemPhoto13 = ShopItemPhoto(
		shop_item_id=item5.id,
		photo_id=photo24.id
		)
	db.session.add(itemPhoto13)
	db.session.commit()

	itemPhoto14 = ShopItemPhoto(
		shop_item_id=item5.id,
		photo_id=photo25.id
		)
	db.session.add(itemPhoto14)
	db.session.commit()

	itemPhoto15 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo10.id
		)
	db.session.add(itemPhoto15)
	db.session.commit()

	itemPhoto16 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo3.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto16)
	db.session.commit()

	itemPhoto17 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo4.id
		)
	db.session.add(itemPhoto17)
	db.session.commit()

	itemPhoto18 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo5.id
		)
	db.session.add(itemPhoto18)
	db.session.commit()

	itemPhoto19 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo6.id
		)
	db.session.add(itemPhoto19)
	db.session.commit()

	itemPhoto20 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo7.id
		)
	db.session.add(itemPhoto20)
	db.session.commit()

	itemPhoto21 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo8.id
		)
	db.session.add(itemPhoto21)
	db.session.commit()

	itemPhoto22 = ShopItemPhoto(
		shop_item_id=item6.id,
		photo_id=photo9.id
		)
	db.session.add(itemPhoto22)
	db.session.commit()

	itemPhoto23 = ShopItemPhoto(
		shop_item_id=item8.id,
		photo_id=photo20.id,
		is_thumbnail=True
		)
	db.session.add(itemPhoto23)
	db.session.commit()

	itemPhoto24 = ShopItemPhoto(
		shop_item_id=item8.id,
		photo_id=photo21.id
		)
	db.session.add(itemPhoto24)
	db.session.commit()

	itemPhoto25 = ShopItemPhoto(
		shop_item_id=item8.id,
		photo_id=photo22.id
		)
	db.session.add(itemPhoto25)
	db.session.commit()


	###############################################################################################################################################################################

	# Insert Press articles
	press1 = Press(title="CONTRIBUTOR MAGAZINE ONLINE", 
		tag_line="EVERY DAY SHOULD BE LIKE TODAY", 
		link="http://contributormagazine.com/fashion-story-fredag/",
		published=datetime(2016,7,8)
		)
	db.session.add(press1)
	db.session.commit()

	press2 = Press(title="METAL MAGAZINE", 
		tag_line="THE TIME OF THE MODERN WOMAN", 
		link="http://metalmagazine.eu/bi/post/interview/22-22-the-time-of-the-modern-woman",
		published=datetime(2016,9,7)
		)
	db.session.add(press2)
	db.session.commit()

	press3 = Press(title="VOGUE ITALIA ONLINE", 
		tag_line="WAITING", 
		link="http://www.vogue.it/vogue-talents/talenti-set/2016/11/30/waiting-benjamin-madgwick-aartthie-mahakuperan/",
		published=datetime(2016,11,30)
		)
	db.session.add(press3)
	db.session.commit()

	###############################################################################################################################################################################

	# Insert PressPhotos
	pressPhoto1 = PressPhoto(
		press_id=press1.id,
		photo_id=photo16.id
		)
	db.session.add(pressPhoto1)
	db.session.commit()

	pressPhoto2 = PressPhoto(
		press_id=press2.id,
		photo_id=photo3.id
		)

	db.session.add(pressPhoto2)
	db.session.commit()

	pressPhoto3 = PressPhoto(
		press_id=press3.id,
		photo_id=photo26.id
		)

	db.session.add(pressPhoto3)
	db.session.commit()

	print "added new entries"

	"""
	SQL commands

	DELETE FROM shop_item_colour;
	DELETE FROM shop_item_photo;
	DELETE FROM shop_item_size;
	DELETE FROM press_photos;
	DELETE FROM colour;
	DELETE FROM photo;
	DELETE FROM press;
	DELETE FROM shop_item;
	DELETE FROM size;

	SELECT * FROM colour;
	SELECT * FROM photo;
	SELECT * FROM press;
	SELECT * FROM press_photos;
	SELECT * FROM shop_item;
	SELECT * FROM shop_item_colour;
	SELECT * FROM shop_item_photo;
	SELECT * FROM shop_item_size;
	SELECT * FROM size;

	DROP TABLE  shop_item_colour;
	DROP TABLE  shop_item_photo;
	DROP TABLE  shop_item_size;
	DROP TABLE press_photos;
	DROP TABLE colour;
	DROP TABLE  photo;
	DROP TABLE  press;
	DROP TABLE  shop_item;
	DROP TABLE  size;
	"""

	return