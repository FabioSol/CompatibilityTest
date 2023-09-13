import os
current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)
db_dir = os.path.dirname(current_dir)
db_name = "/testing.db"
path = db_dir + db_name
