from peewee import *
import datetime
import os
	
class BaseModel(Model):
	class Meta:
		database = SqliteDatabase(os.getenv("GETTR_DATA_PATH", default="./data.db"))

class Post(BaseModel):
	id = CharField(unique=True)
	text = TextField()
	hashtags = TextField()
	uid = TextField()
	cdate = IntegerField()
	udate = IntegerField()
	poster = TextField()
 