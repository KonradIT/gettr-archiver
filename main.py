import Archiver
import os


if not os.path.isfile(os.getenv("GETTR_DATA_PATH", default="./data.db")):
	Archiver.GettrArchiver.setup(os.getenv("GETTR_DATA_PATH", default="./data.db"))

a = Archiver.GettrArchiver(db_file_path=os.getenv("GETTR_DATA_PATH", default="./data.db"))
a.run()