from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from Game.queries import get_user_by_name


class UserLoginForm(FlaskForm):
    name = StringField('Username',
                       validators=[DataRequired(), Length(min=2, max=50)],
                       render_kw=dict(placeholder='Username'))
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw=dict(placeholder='Password'))
    submit = SubmitField('Login')

    def validate_password(self, field):
        user = get_user_by_name(self.name.data)
        if user is None:
            raise ValidationError(f'User name "{self.name.data}" does not exist.')
        if user.password != self.password.data:
            raise ValidationError(f'User name or password are incorrect.')


class UserSignupForm(FlaskForm):
    name = StringField('Username',
                       validators=[DataRequired(), Length(min=2, max=50)],
                       render_kw=dict(placeholder='Username'))
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw=dict(placeholder='Password'))
    password_repeat = PasswordField('Repeat Password',
                                    validators=[DataRequired()],
                                    render_kw=dict(placeholder='Password'))
    submit = SubmitField('Sign up')

    go_to_login = SubmitField('Log in with existing user')

    def validate_user_name(self, field):
        user = get_user_by_name(self.name.data)
        if user:
            raise ValidationError(f'User name "{self.name.data}" already in use.')

    def validate_password_repeat(self, field):
        if not self.password.data == self.password_repeat.data:
            raise ValidationError(f'Provided passwords do not match.')


class PlayForm(FlaskForm):
    #One submit button and one stringfield
    #username1 = StringField('User1 name',
    #                   validators=[DataRequired(), Length(min=2, max=50)],
    #                   render_kw=dict(placeholder='Playername'))
    #username2 = StringField('User2 name',
    #                   validators=[DataRequired(), Length(min=2, max=50)],
    #                   render_kw=dict(placeholder='Playername'))
    playername = StringField('Playername for user 1',
                       validators=[DataRequired(), Length(min=2, max=50)],
                       render_kw=dict(placeholder='Playername'))
    submit = SubmitField('Submit')
    #submituser2 = SubmitField('Lock in')
    #måske ligesom validate_user_name hav spillogik her?



