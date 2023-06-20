from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

##------------------------------Flaskforms
class EditForm(FlaskForm):
    img_source = StringField(label="Please paste url to car image", validators=[DataRequired()])
    submit = SubmitField(label="Update")
