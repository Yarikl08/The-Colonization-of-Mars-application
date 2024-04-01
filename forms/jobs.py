from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField("Job Title", validators=[DataRequired()])
    team_leader = IntegerField("Team Leader id")
    work_size = StringField("Work Size")
    collaborators = StringField("Collaborators")
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')