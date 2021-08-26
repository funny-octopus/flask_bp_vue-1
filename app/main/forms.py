from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField

class UploadDomainList(FlaskForm):
    upload_filename = FileField(validators=[FileRequired()])
    upload_submit = SubmitField("Загрузить")