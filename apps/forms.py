# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SelectField
)
from wtforms import validators
from wtforms.fields.html5 import (
    EmailField,
    DateField
)
class JoinForm(Form):
    email = EmailField(
        [validators.data_required(u'이메일을 입력하시기 바랍니다.')],
        description={'placeholder': u'이메일 입력'}
    )
    password = PasswordField(
        [validators.data_required(u'패스워드를 입력하시기 바랍니다.'),
        validators.EqualTo('confirm_password', message=u'패스워드가 일치하지않습니다.')],
        description={'placeholder': u'패스워드 입력'}
    )
    confirm_password = PasswordField(
        
        [validators.data_required(u'패스워드를 한번 더 입력하세요.')],
        description={'placeholder': u'패스워드 재입력'}
    )
    name = StringField(
        
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름 입력'}
    )
    

class LoginForm(Form):
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력해주세요.')],
        description={'placeholder': u'이메일 입력'}
    )
    password = PasswordField(
        u'패스워드',
        [validators.data_required(u'패스워드를 입력해주세요.')],
        description={'placeholder': u'패스워드 입력'}
    )