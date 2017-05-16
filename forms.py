from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Required

import models

class ShopItemForm(FlaskForm):
	size_id = SelectField('size_id', default=0, validators=[DataRequired(message="Please select a size.")], coerce=int)
	colour_id = SelectField('colour_id', default=0, validators=[DataRequired(message="Please select a size.")], coerce=int)


class UserForm(FlaskForm):
	email = StringField('E-MAIL', validators=[DataRequired(message=(u'Please enter your email address')),
													 Email(message=(u'Please enter a valid email address'))])
	first_name = StringField('FIRST NAME', validators=[DataRequired(message=(u'Please enter your first name'))])
	last_name = StringField('LAST NAME', validators=[DataRequired(message=(u'Please enter your last name'))])
	
class PaymentForm(FlaskForm):
	email = StringField('E-MAIL', validators=[DataRequired(message=(u'Please enter your email address')),
													 Email(message=(u'Please enter a valid email address'))])
	
	# Delivery details
	delivery_first_name = StringField('FIRST NAME', validators=[DataRequired(message=(u'Please enter your first name'))])
	delivery_last_name = StringField('LAST NAME', validators=[DataRequired(message=(u'Please enter your last name'))])

	delivery_street = StringField('ADDRESS', validators=[DataRequired()])
	delivery_city = StringField('CITY', validators=[DataRequired()])
	delivery_zip = StringField('POSTCODE', validators=[DataRequired()])
	delivery_country = StringField('COUNTRY', validators=[DataRequired()])

	# Billing details
	billing_first_name = StringField('FIRST NAME', validators=[DataRequired(message=(u'Please enter your first name'))])
	billing_last_name = StringField('LAST NAME', validators=[DataRequired(message=(u'Please enter your last name'))])

	billing_street = StringField('ADDRESS', validators=[DataRequired()])
	billing_city = StringField('CITY', validators=[DataRequired()])
	billing_zip = StringField('POSTCODE', validators=[DataRequired()])
	billing_country = StringField('COUNTRY', validators=[DataRequired()])



# from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

# import models

# def validate_size(size_id):
# 	try:
# 		size = models.Size.query.filter_by(id=size_id).one()
# 	except (MultipleResultsFound, NoResultFound):
# 		return False
# 	if size is None:
# 		return False

# 	return size_id

# def validate_colour(colour_id):
# 	try:
# 		colour = models.Colour.query.filter_by(id=colour_id).one()
# 	except (MultipleResultsFound, NoResultFound):
# 		return False
# 	if colour is None:
# 		return False

# 	return colour_id