# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from bpapp.user.forms import LogEntryForm
from bpapp.utils import flash_errors

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/log_entry', methods=['GET', 'POST'])
@login_required
def log_entry():
    """List log_entry."""
    form = LogEntryForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        # User.create(username=form.username.data, email=form.email.data, password=form.password.data, first_name=form.first_name.data, last_name=form.last_name.data, active=True)
        flash('Your entry as been logged', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('users/log_entry.html', form=form)

@blueprint.route('/log_list')
@login_required
def log_list():
    """List log_entry."""
    return render_template('users/log_list.html')
