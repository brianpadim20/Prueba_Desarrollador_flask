from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class AddItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    price = FloatField('Price', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired(), Length(min=1, max=17)])
    serial_number = StringField('Serial Number', validators=[DataRequired(), Length(min=1, max=50)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Add Item')

class EditItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    price = FloatField('Price', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[DataRequired(), Length(min=1, max=17)])
    serial_number = StringField('Serial Number', validators=[DataRequired(), Length(min=1, max=50)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Save Changes')
