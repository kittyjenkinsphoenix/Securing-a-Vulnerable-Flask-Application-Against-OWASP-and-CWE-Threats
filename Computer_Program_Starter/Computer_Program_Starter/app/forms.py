from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Regexp

# Form For User Registration
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6,max=45)])
    # Password Must Be Between 12 And 25 Characters Long, Contain At Least One Uppercase Letter, One Lowercase Letter, One Number, And One Special Character
    password = PasswordField('Password', 
                         validators=[
                             DataRequired(), 
                             Length(min=12, max=25), 
                             Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,25}$', 
                                    message='Password Must Be 12-25 Characters Long And Include At Least One Uppercase Letter, One Lowercase Letter, One Number, And One Special Character.')
                         ])
    repeatedPassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    biography = StringField('Biography', validators=[Length(max=150)])
    submit = SubmitField('Register')

    def validate_email(self, email):
        blacklist = ['user1@email.com', 'mod1@email.com', 'admin1@email.com']
        if email.data.lower() in blacklist:
            raise ValidationError('This Email Is Not Allowed. Please Choose A Different One.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')