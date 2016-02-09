# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
import datetime as dt
from .models import User, PressureLog


class RegisterForm(Form):
    """Register form."""

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    first_name = StringField('First name', validators=[Length(min=1, max=30)])
    last_name = StringField('Last name', validators=[Length(min=1, max=30)])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('Username already registered')
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already registered')
            return False
        return True


class LogEntryForm(Form):
    """
        Blood pressure diary entry form
    """

    systolic = IntegerField(label='Systolic', validators=[DataRequired(), NumberRange(min=30, max=300)])
    diastolic = IntegerField(label='Diastolic', validators=[DataRequired(), NumberRange(min=30, max=300)])
    heart_beats = IntegerField(label='Heart beats', validators=[DataRequired(), NumberRange(min=30, max=300)])

    measured_at = DateTimeField(label='Date time', validators=[DataRequired()],
                                format='%Y-%m-%d %H:%M', default=dt.datetime.utcnow)