#-*- coding:utf-8 -*-
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
import models
# 定义的表单都需要继承自FlaskForm

	
class LoginForm(FlaskForm):
    # 域初始化时，第一个参数是设置label属性的
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    
    
    """
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    """

    username = StringField('Username', validators=[
        Required(), Length(1, 64)])
    gender = StringField('Gender',validators=[
        Required(), Length(1, 4)])
    country = StringField('Country',validators=[
        Required(), Length(1, 10)])
    province = StringField('Province',validators=[
        Required(), Length(1, 10)])
    city = StringField('City',validators=[
        Required(), Length(1, 20)])

    moreaddress = StringField('MoreAddress',validators=[
        Required(), Length(1, 20)])
    submit = SubmitField('Register')


    def validate_email(self, field):
        if models.User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if models.User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField('Update Password')


class PostForm(FlaskForm):
    body=StringField("What's on your mind?", validators=[Required()])
    file = StringField('picture_place')
    submit = SubmitField('new show submit')


class ReceiveForm(FlaskForm):
    mail_ID=IntegerField("Your mail ID", validators=[Required()])
    submit = SubmitField('mail ID submit')


class EmailForm(FlaskForm):
    choose_area_rd=StringField("choose_area_rd?", validators=[Required()])
    choose_sex_rd = StringField('choose_sex_rd')
    submit = SubmitField('new show submit')

class Search(FlaskForm):
    search = StringField('search')
    submit = SubmitField('new show submit')

class UserForm(FlaskForm):
    user = StringField('user')
    submit = SubmitField('new show submit')