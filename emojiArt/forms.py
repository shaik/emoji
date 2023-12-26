from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, SubmitField
from flask_wtf.file import FileAllowed
from .config import Config

class UploadForm(FlaskForm):
    file = FileField('Image File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'])])
    grid_width = SelectField('Grid Width', choices=[(str(width), str(width)) for width in sorted(Config.ALLOWED_GRID_WIDTHS)])
    submit = SubmitField('Upload')
