# -*- coding: utf-8 -*-
from flask import jsonify, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, \
	 check_password_hash
from sqlalchemy import desc
from apps import app, db
from google.appengine.ext import db as gdb
import datetime
from sqlalchemy import desc,asc

from apps.forms import JoinForm, LoginForm
from apps.models import (
	User,
	Comment,
	Location
	)

@app.route('/', methods=['GET', 'POST'])
def main():
	
	return render_template('main.html', form2 = JoinForm(), form = LoginForm())

@app.route('/index', methods=['GET', 'POST'])
def index():

	return render_template('index.html', form2 = JoinForm(), form = LoginForm(), city_title=u"서울시")



# @error Handlers
#
# Handle 404 errors

@app.route('/', methods=['GET', 'POST'])
def search():
	if request.method == 'GET':
		input_localname = request.args['city_input']
		local_info = Location.query.get(local_name)
		if local_info == input_localname:
			return render_template('index.html', local_info=local_info)
		else:
			return render_template('index.html')
	else:
		render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
	return render_template('error/404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return render_template('error/500.html'), 500
