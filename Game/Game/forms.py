from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PlayForm(FlaskForm):
    playername = StringField('',
                       validators=[DataRequired(), Length(min=2, max=50)],
                       render_kw=dict(placeholder='Player Name'))
    submit = SubmitField('SUBMIT')

class StartNewGameForm(FlaskForm):
    submit = SubmitField('START NEW GAME')

class StartGameForm(FlaskForm):
    submit = SubmitField('START THE GAME')
