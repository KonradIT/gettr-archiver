from peewee import *
from Archiver import models
from gogettr import PublicClient
import signal
import sys

class GettrArchiver:
	
	def __init__(self, db_file_path: str = "./data.db"):
		self.db = SqliteDatabase(db_file_path)

	@staticmethod
	def setup(db_file_path: str = "./data.db"):
		db = SqliteDatabase(db_file_path)
		db.connect()
		db.create_tables([models.Post])
  
	def run(self):
     
		def quit(signal, frame):
			self.db.close()
			print("Gracefully exiting...")
			sys.exit(0)
   
		signal.signal(signal.SIGINT, quit)
  
		client = PublicClient()  
		for post in client.all(
				first="pxnbn",
				last=None,
				max=None,
				order="up",
				type="posts",
				workers=10,
			):
			print("Saving post...")
   
			try:
				if post is None:
					pass
				post_in_db = models.Post.create(
					id=post.get("_id"),
					text = post.get("txt"),
					hashtags = "" if post.get("htgs") is None or len(post.get("htgs")) == 0 else ",".join(post.get("htgs")),
					uid = post.get("uid"),
					cdate = post.get("cdate"),
					udate = post.get("udate"),
					poster = post.get("uinf").get("username")
				)
				print(post_in_db)
			except:
				pass
   
		self.db.close()