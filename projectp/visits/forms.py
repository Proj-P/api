from wtforms import IntegerField, DateField, Form
from wtforms.validators import InputRequired


class VisitForm(Form):
    start_time = IntegerField('start_time', validators=[InputRequired()])
    end_time = IntegerField('end_time', validators=[InputRequired()])


class DateForm(Form):
    start = DateField('start', validators=[InputRequired()])
    end = DateField('end', validators=[InputRequired()])
