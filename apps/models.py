"""
models.py

"""
from apps import db


class User(db.Model):
	email = db.Column(db.String(255), primary_key = True)
	password = db.Column(db.String(32))
	name = db.Column(db.String(45))
	birthday = db.Column(db.DateTime())
	age = db.Column(db.Integer)
	written_comment = db.Column(db.String(255))
	likeclicked_comment = db.Column(db.String(255))
	
class Comment(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	location_id =  db.Column(db.String(100), db.ForeignKey('Location.id'))
	content = db.Column(db.String(150))
	user_email = db.Column(db.String(255), db.ForeignKey('User.email'))	
	like = db.Column(db.Integer)
	dislike = db.Column(db.Integer)
	created_time = db.Column(db.DateTime(), default=db.func.now())

class Location(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	comment = db.Column(db.String(150))
	hashtag = db.Column(db.String(45))
	local_name = db.Column(db.String(100))		
