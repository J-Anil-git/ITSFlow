from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TicketForm(FlaskForm):
    staff_name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    department = SelectField("Department", coerce=int,
                             validators=[DataRequired(message="Choose your department.")])
    description = TextAreaField("Issue description", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField("Send ticket")
